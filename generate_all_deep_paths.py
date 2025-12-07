#!/usr/bin/env python3
"""
Optimized Deep Path Generator for All Drugs

This script generates comprehensive 2-5 hop paths for all Amgen/Horizon drugs.
Optimizations:
1. Load KG and embeddings ONCE at startup
2. Batch process all drugs efficiently
3. Use numpy for fast attention computation
4. Limit exploration with smart pruning
"""

import pandas as pd
import numpy as np
from collections import defaultdict, deque
import json
import pickle
import time
import os
import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import torch

# ============================================================================
# GLOBAL DATA (loaded once)
# ============================================================================

class KGData:
    """Singleton-like class to hold KG data loaded once."""
    _instance = None
    
    def __init__(self):
        self.nodes_df = None
        self.node_idx_to_info = {}
        self.adj = None
        self.disease_indices = set()
        self.embeddings = {}
        self.global_to_type_idx = {}
        self.loaded = False
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def load(self, data_dir='./data', model_dir='./model_ckpt'):
        """Load all data once."""
        if self.loaded:
            return
        
        print("=" * 80)
        print("LOADING KNOWLEDGE GRAPH AND EMBEDDINGS (ONE TIME)")
        print("=" * 80)
        
        start = time.time()
        
        # Load nodes
        print("\n[1/4] Loading nodes...")
        self.nodes_df = pd.read_csv(f'{data_dir}/node.csv', sep='\t')
        
        type_to_nodes = defaultdict(list)
        for _, row in self.nodes_df.iterrows():
            idx = int(row['node_index'])
            node_type = str(row['node_type'])
            self.node_idx_to_info[idx] = {
                'id': str(row['node_id']),
                'type': node_type,
                'name': str(row['node_name'])
            }
            type_to_nodes[node_type].append(idx)
            if node_type == 'disease':
                self.disease_indices.add(idx)
        
        # Create type index mapping
        for node_type, indices in type_to_nodes.items():
            for emb_idx, global_idx in enumerate(indices):
                self.global_to_type_idx[global_idx] = (node_type, emb_idx)
        
        print(f"  Loaded {len(self.node_idx_to_info)} nodes, {len(self.disease_indices)} diseases")
        
        # Load KG edges
        print("\n[2/4] Building adjacency list...")
        kg_df = pd.read_csv(f'{data_dir}/kg.csv', low_memory=False)
        
        self.adj = defaultdict(list)
        for _, row in kg_df.iterrows():
            x_idx = int(row['x_index'])
            y_idx = int(row['y_index'])
            self.adj[x_idx].append(y_idx)
            self.adj[y_idx].append(x_idx)
        
        print(f"  Built adjacency for {len(self.adj)} nodes")
        
        # Load embeddings
        print("\n[3/4] Loading TxGNN embeddings...")
        emb_file = f'{model_dir}/node_emb.pkl'
        if os.path.exists(emb_file):
            with open(emb_file, 'rb') as f:
                node_emb_dict = pickle.load(f)
            
            for k, v in node_emb_dict.items():
                if isinstance(v, torch.Tensor):
                    self.embeddings[k] = v.detach().cpu().numpy()
                else:
                    self.embeddings[k] = v
                print(f"    {k}: {self.embeddings[k].shape}")
        else:
            print(f"  Warning: {emb_file} not found, using default attention scores")
        
        # Load drug list from multiple sources
        print("\n[4/4] Loading drug information...")
        self.drug_info = {}
        
        # Method 1: Load from kg_drug_catalog.csv (most complete)
        catalog_file = './repurpose_out/kg_drug_catalog.csv'
        if os.path.exists(catalog_file):
            catalog_df = pd.read_csv(catalog_file)
            for _, row in catalog_df.iterrows():
                drug_id = str(row['node_id'])
                drug_name = str(row['node_name'])
                # Find in nodes
                drug_nodes = self.nodes_df[
                    (self.nodes_df['node_id'] == drug_id) & 
                    (self.nodes_df['node_type'] == 'drug')
                ]
                if len(drug_nodes) > 0:
                    self.drug_info[drug_id] = {
                        'idx': int(drug_nodes.iloc[0]['node_index']),
                        'name': drug_name
                    }
        
        # Method 2: Filter to only Amgen/Horizon drugs from present_drugs.csv
        present_file = './repurpose_out/present_drugs.csv'
        if os.path.exists(present_file):
            present_df = pd.read_csv(present_file)
            present_names = set(present_df['present_generic'].str.lower())
            
            # Filter drug_info to only include Amgen/Horizon drugs
            filtered_info = {}
            for drug_id, info in self.drug_info.items():
                if info['name'].lower() in present_names:
                    filtered_info[drug_id] = info
            
            if filtered_info:
                self.drug_info = filtered_info
        
        print(f"  Found {len(self.drug_info)} Amgen/Horizon drugs in KG")
        
        self.loaded = True
        print(f"\n✅ Data loading completed in {time.time()-start:.1f}s")
    
    def get_embedding(self, global_idx):
        """Get embedding for a global node index."""
        if global_idx not in self.global_to_type_idx:
            return None
        node_type, type_idx = self.global_to_type_idx[global_idx]
        if node_type not in self.embeddings:
            return None
        emb_array = self.embeddings[node_type]
        if type_idx >= len(emb_array):
            return None
        return emb_array[type_idx]
    
    def compute_attention(self, idx1, idx2):
        """Compute attention score between two nodes."""
        emb1 = self.get_embedding(idx1)
        emb2 = self.get_embedding(idx2)
        
        if emb1 is None or emb2 is None:
            return 0.5  # Default
        
        norm1 = np.linalg.norm(emb1)
        norm2 = np.linalg.norm(emb2)
        if norm1 < 1e-8 or norm2 < 1e-8:
            return 0.5
        
        sim = np.dot(emb1, emb2) / (norm1 * norm2)
        return float((sim + 1) / 2)


def find_deep_paths(kg: KGData, drug_idx: int, max_depth: int = 5, 
                    max_paths_per_depth: int = 500, max_frontier: int = 50000):
    """
    Find deep paths from drug to diseases using optimized BFS.
    
    Args:
        kg: KGData instance
        drug_idx: Starting drug node index
        max_depth: Maximum path depth (default 5)
        max_paths_per_depth: Max paths to keep per depth level
        max_frontier: Max frontier size to prevent memory explosion
    
    Returns:
        List of path dictionaries
    """
    all_paths = []
    
    # Track frontier at each level: {node_idx: [paths_to_reach_it]}
    frontier = {drug_idx: [(drug_idx,)]}
    visited_global = {drug_idx}
    
    for depth in range(1, max_depth + 1):
        next_frontier = defaultdict(list)
        paths_found = 0
        
        for curr_idx, paths_to_curr in frontier.items():
            # Limit neighbors to explore
            neighbors = kg.adj[curr_idx][:100]  # Cap at 100 neighbors
            
            for neighbor_idx in neighbors:
                if neighbor_idx in visited_global:
                    continue
                
                neighbor_info = kg.node_idx_to_info.get(neighbor_idx, {})
                neighbor_type = neighbor_info.get('type', '')
                
                for path in paths_to_curr[:3]:  # Keep top 3 paths per node
                    new_path = path + (neighbor_idx,)
                    
                    # If disease found, save path
                    if neighbor_idx in kg.disease_indices:
                        if paths_found < max_paths_per_depth:
                            all_paths.append({
                                'hops': depth,
                                'path_indices': new_path
                            })
                            paths_found += 1
                    else:
                        # Continue exploring non-disease nodes
                        if neighbor_type in ['gene/protein', 'biological_process', 
                                            'pathway', 'anatomy', 'drug', 
                                            'cellular_component', 'molecular_function']:
                            if len(next_frontier[neighbor_idx]) < 5:
                                next_frontier[neighbor_idx].append(new_path)
        
        # Update visited and frontier
        visited_global.update(next_frontier.keys())
        
        # Prune frontier if too large
        if len(next_frontier) > max_frontier:
            # Keep nodes with shortest paths
            items = list(next_frontier.items())
            items.sort(key=lambda x: len(x[1][0]) if x[1] else 999)
            next_frontier = dict(items[:max_frontier])
        
        frontier = dict(next_frontier)
        
        if len(frontier) == 0:
            break
    
    return all_paths


def score_paths(kg: KGData, paths: list) -> list:
    """Score paths with attention weights."""
    scored_paths = []
    
    for path_dict in paths:
        indices = path_dict['path_indices']
        hops = path_dict['hops']
        
        # Build node info
        nodes = []
        for idx in indices:
            info = kg.node_idx_to_info.get(idx, {})
            nodes.append({
                'idx': int(idx),
                'name': info.get('name', str(idx)),
                'type': info.get('type', 'unknown')
            })
        
        # Compute attention scores
        attention_scores = []
        for i in range(len(indices) - 1):
            att = kg.compute_attention(indices[i], indices[i+1])
            attention_scores.append(round(att, 4))
        
        avg_attention = sum(attention_scores) / len(attention_scores) if attention_scores else 0.5
        length_penalty = 1.0 / (hops ** 0.5)
        combined_score = avg_attention * length_penalty
        
        scored_paths.append({
            'hops': hops,
            'nodes': nodes,
            'edges': ['edge'] * (len(nodes) - 1),
            'attention_scores': attention_scores,
            'avg_attention': round(avg_attention, 4),
            'min_attention': round(min(attention_scores), 4) if attention_scores else 0,
            'max_attention': round(max(attention_scores), 4) if attention_scores else 0,
            'length_penalty': round(length_penalty, 4),
            'combined_score': round(combined_score, 4)
        })
    
    # Sort by combined score
    scored_paths.sort(key=lambda x: -x['combined_score'])
    
    return scored_paths


def process_drug(drug_id: str, drug_idx: int, kg: KGData, output_dir: str, 
                 max_depth: int = 5, max_paths: int = 2000):
    """
    Process a single drug to generate deep paths.
    
    Args:
        drug_id: Drug ID (e.g., 'DB12530')
        drug_idx: Drug node index in KG
        kg: KGData instance
        output_dir: Output directory
        max_depth: Maximum path depth
        max_paths: Maximum paths to keep
    
    Returns:
        Dict with processing results
    """
    start = time.time()
    
    # Find paths
    raw_paths = find_deep_paths(kg, drug_idx, max_depth=max_depth, 
                                max_paths_per_depth=max_paths // max_depth)
    
    # Score paths
    scored_paths = score_paths(kg, raw_paths)
    
    # Keep top paths
    scored_paths = scored_paths[:max_paths]
    
    # Group by disease for statistics
    by_disease = defaultdict(list)
    by_hops = defaultdict(list)
    for path in scored_paths:
        disease_name = path['nodes'][-1]['name']
        by_disease[disease_name].append(path)
        by_hops[path['hops']].append(path)
    
    # Compute statistics
    all_att = [p['avg_attention'] for p in scored_paths]
    stats = {
        'mean_attention': round(np.mean(all_att), 4) if all_att else 0,
        'std_attention': round(np.std(all_att), 4) if all_att else 0,
        'min_attention': round(np.min(all_att), 4) if all_att else 0,
        'max_attention': round(np.max(all_att), 4) if all_att else 0
    }
    
    # Build output
    drug_info = kg.node_idx_to_info.get(drug_idx, {})
    output = {
        'drug': {
            'id': drug_id,
            'name': drug_info.get('name', drug_id),
            'type': 'drug'
        },
        'total_paths': len(scored_paths),
        'unique_diseases': len(by_disease),
        'statistics': stats,
        'score_explanation': {
            'avg_attention': 'Average cosine similarity of TxGNN embeddings (0-1)',
            'length_penalty': '1/sqrt(hops)',
            'combined_score': 'avg_attention * length_penalty'
        },
        'paths_by_hops': {str(k): len(v) for k, v in by_hops.items()},
        'global_top_100': scored_paths[:100],
        'top_paths_per_disease': {
            d: paths[:10] for d, paths in list(by_disease.items())[:200]
        }
    }
    
    # Save to file
    drug_name_clean = drug_info.get('name', drug_id).lower().replace(' ', '_').replace('/', '_')
    output_file = os.path.join(output_dir, f'{drug_name_clean}_scored_paths.json')
    with open(output_file, 'w') as f:
        json.dump(output, f)
    
    elapsed = time.time() - start
    
    return {
        'drug_id': drug_id,
        'drug_name': drug_info.get('name', drug_id),
        'total_paths': len(scored_paths),
        'unique_diseases': len(by_disease),
        'output_file': output_file,
        'elapsed': elapsed
    }


def main():
    parser = argparse.ArgumentParser(description='Generate deep paths for all drugs')
    parser.add_argument('--data_dir', default='./data', help='Data directory')
    parser.add_argument('--model_dir', default='./model_ckpt', help='Model checkpoint directory')
    parser.add_argument('--output_dir', default='./drugExplorer/data', help='Output directory')
    parser.add_argument('--max_depth', type=int, default=5, help='Max path depth')
    parser.add_argument('--max_paths', type=int, default=2000, help='Max paths per drug')
    parser.add_argument('--drug', type=str, default=None, help='Process single drug (optional)')
    args = parser.parse_args()
    
    print("=" * 80)
    print("DEEP PATH GENERATOR FOR ALL DRUGS")
    print("=" * 80)
    
    total_start = time.time()
    
    # Load KG data (once)
    kg = KGData.get_instance()
    kg.load(args.data_dir, args.model_dir)
    
    # Get drugs to process
    if args.drug:
        drug_info = kg.drug_info.get(args.drug)
        if drug_info is None:
            print(f"Error: Drug {args.drug} not found in KG")
            return
        drugs_to_process = {args.drug: drug_info}
    else:
        drugs_to_process = kg.drug_info
    
    print(f"\n{'='*80}")
    print(f"PROCESSING {len(drugs_to_process)} DRUGS")
    print(f"{'='*80}")
    
    os.makedirs(args.output_dir, exist_ok=True)
    
    results = []
    for i, (drug_id, drug_info) in enumerate(drugs_to_process.items(), 1):
        drug_idx = drug_info['idx']
        drug_name = drug_info['name']
        print(f"\n[{i}/{len(drugs_to_process)}] Processing {drug_id} ({drug_name})...")
        
        result = process_drug(
            drug_id=drug_id,
            drug_idx=drug_idx,
            kg=kg,
            output_dir=args.output_dir,
            max_depth=args.max_depth,
            max_paths=args.max_paths
        )
        
        results.append(result)
        print(f"  ✅ {result['total_paths']} paths to {result['unique_diseases']} diseases "
              f"in {result['elapsed']:.1f}s")
    
    # Summary
    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    
    total_paths = sum(r['total_paths'] for r in results)
    total_diseases = sum(r['unique_diseases'] for r in results)
    total_time = time.time() - total_start
    
    print(f"\nProcessed {len(results)} drugs:")
    print(f"  Total paths generated: {total_paths:,}")
    print(f"  Total unique diseases: {total_diseases:,}")
    print(f"  Total time: {total_time:.1f}s ({total_time/len(results):.1f}s per drug)")
    
    # Save summary
    summary_file = os.path.join(args.output_dir, 'deep_paths_summary.json')
    with open(summary_file, 'w') as f:
        json.dump({
            'generated_at': time.strftime('%Y-%m-%d %H:%M:%S'),
            'total_drugs': len(results),
            'total_paths': total_paths,
            'total_time_seconds': round(total_time, 1),
            'drugs': results
        }, f, indent=2)
    
    print(f"\n✅ Summary saved to: {summary_file}")
    print(f"✅ All path files saved to: {args.output_dir}")


if __name__ == '__main__':
    main()

