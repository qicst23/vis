import json
import pandas as pd
import numpy as np
import os
import sys
from flask import current_app, g

class JsonDatabase:
    """JSON-based database implementation for Drug Explorer quickstart.
    
    This class provides the same interface as Neo4jApp but reads from JSON files
    instead of connecting to a Neo4j database.
    """
    def __init__(self, server='attention', data_folder='./data'):
        """Initialize the JSON database.
        
        Args:
            server: Model type ('attention' or 'graphmask')
            data_folder: Path to data folder containing JSON files
        """
        self.data_folder = data_folder
        self.server = server
        self.current_disease = None
        self.drugs = None
        
        # Load all JSON data files
        self._load_data()
        
    def _load_data(self):
        """Load all required JSON data files."""
        try:
            # Load node name dictionary
            node_dict_file = f"{self.server}_node_name_dict.json"
            with open(os.path.join(self.data_folder, node_dict_file), 'r') as f:
                self.node_name_dict = json.load(f)
            
            # Load richer node info if available
            self.node_info = {}
            node_info_file = os.path.join(self.data_folder, 'attention_node_info.json')
            if os.path.exists(node_info_file):
                with open(node_info_file, 'r') as f:
                    self.node_info = json.load(f)
                    print(f"Loaded attention_node_info.json with {len(self.node_info)} nodes")
                    
                    # Update node_name_dict with richer info
                    for node_id, info in self.node_info.items():
                        node_type = info.get('type')
                        node_name = info.get('name')
                        
                        if node_type and node_name:
                            if node_type not in self.node_name_dict:
                                self.node_name_dict[node_type] = {}
                            self.node_name_dict[node_type][node_id] = node_name

            # Load edge types
            with open(os.path.join(self.data_folder, 'edge_types.json'), 'r') as f:
                self.edge_types = json.load(f)
            
            # Load node types
            with open(os.path.join(self.data_folder, 'node_types.json'), 'r') as f:
                self.node_types = json.load(f)
            
            # Load drug index mapping
            with open(os.path.join(self.data_folder, 'drug_idx2id.json'), 'r') as f:
                self.drug_idx2id = json.load(f)
            
            # Load drug t-SNE coordinates
            with open(os.path.join(self.data_folder, 'drug_tsne.json'), 'r') as f:
                self.drug_tsne = json.load(f)
            
            # Load meta path data
            with open(os.path.join(self.data_folder, 'meta_path_json.json'), 'r') as f:
                self.meta_path_data = json.load(f)

            # Load disease node IDs and update node_name_dict
            disease_node_ids_file = os.path.join(self.data_folder, 'disease_node_ids.json')
            if os.path.exists(disease_node_ids_file):
                with open(disease_node_ids_file, 'r') as f:
                    disease_name_to_id = json.load(f)
                    # Invert to ID -> Name
                    disease_id_to_name = {v: k for k, v in disease_name_to_id.items()}
                    
                    # Ensure 'disease' key exists
                    if 'disease' not in self.node_name_dict:
                        self.node_name_dict['disease'] = {}
                        
                    # Update node_name_dict with names from disease_node_ids.json
                    self.node_name_dict['disease'].update(disease_id_to_name)
                    print(f"Updated node_name_dict with {len(disease_id_to_name)} diseases from disease_node_ids.json")

                
            # Load drug-to-disease predictions
            predictions_file = os.path.join(self.data_folder, 'your_predictions.csv')
            if os.path.exists(predictions_file):
                self.predictions_df = pd.read_csv(predictions_file)
                if 'drug_id' not in self.predictions_df.columns:
                    print("Warning: your_predictions.csv missing 'drug_id' column")
                
                # Create disease_id to disease_node_id map
                self.disease_id_map = {}
                if 'disease_id' in self.predictions_df.columns and 'disease_node_id' in self.predictions_df.columns:
                    # Drop duplicates to get unique mappings
                    mapping_df = self.predictions_df[['disease_id', 'disease_node_id']].drop_duplicates()
                    for _, row in mapping_df.iterrows():
                        # Skip NaN values
                        if pd.isna(row['disease_id']) or pd.isna(row['disease_node_id']):
                            continue
                            
                        d_id = str(row['disease_id'])
                        if isinstance(row['disease_id'], float) and not pd.isna(row['disease_id']):
                            d_id = str(int(row['disease_id']))
                            
                        dn_id = str(row['disease_node_id'])
                        if isinstance(row['disease_node_id'], float) and not pd.isna(row['disease_node_id']):
                            dn_id = str(int(row['disease_node_id']))
                            
                        self.disease_id_map[d_id] = dn_id
                    print(f"Created disease_id_map with {len(self.disease_id_map)} entries")
            else:
                print(f"Warning: {predictions_file} not found")
                self.predictions_df = pd.DataFrame()
                self.disease_id_map = {}
            
            # Load attention data from attention_all.csv
            attention_file = os.path.join(self.data_folder, 'attention_all.csv')
            if os.path.exists(attention_file):
                self.attention_df = pd.read_csv(attention_file)
                print(f"Loaded attention_all.csv with {len(self.attention_df)} edges")
                
                # Convert node IDs to strings for consistency
                self.attention_df['x_id'] = self.attention_df['x_id'].astype(str)
                self.attention_df['y_id'] = self.attention_df['y_id'].astype(str)
                
                # Create indices for fast lookup
                self.attention_by_source = {}
                self.attention_by_target = {}
                
                for idx, row in self.attention_df.iterrows():
                    # Index by source node
                    key = (str(row['x_id']), row['x_type'])
                    if key not in self.attention_by_source:
                        self.attention_by_source[key] = []
                    self.attention_by_source[key].append(row)
                    
                    # Index by target node  
                    key = (str(row['y_id']), row['y_type'])
                    if key not in self.attention_by_target:
                        self.attention_by_target[key] = []
                    self.attention_by_target[key].append(row)
                    
                print(f"Indexed {len(self.attention_by_source)} source nodes and {len(self.attention_by_target)} target nodes")
            else:
                print(f"Warning: {attention_file} not found")
                self.attention_df = pd.DataFrame()
                self.attention_by_source = {}
                self.attention_by_target = {}
            
            # Load precomputed paths
            precomputed_paths_file = os.path.join(self.data_folder, 'precomputed_paths.json')
            if os.path.exists(precomputed_paths_file):
                with open(precomputed_paths_file, 'r') as f:
                    self.precomputed_paths = json.load(f)
                print(f"Loaded precomputed_paths.json with {len(self.precomputed_paths)} entries")
            else:
                self.precomputed_paths = {}
            
            # Load subgraphs
            subgraphs_file = os.path.join(self.data_folder, 'subgraphs.json')
            if os.path.exists(subgraphs_file):
                with open(subgraphs_file, 'r') as f:
                    self.subgraphs = json.load(f)
                print(f"Loaded subgraphs.json with {len(self.subgraphs)} drug-disease pairs")
            else:
                self.subgraphs = {}
            
            print(f"Successfully loaded JSON data from {self.data_folder}")
            print(f"Node types available: {list(self.node_name_dict.keys())}")
            
            
        except Exception as e:
            print(f"Error loading JSON data: {e}")
            raise
    
    def create_session(self):
        """Compatibility method - no session needed for JSON backend."""
        pass
    
    def close_session(self):
        """Compatibility method - no session to close for JSON backend."""
        pass
    
    def close_driver(self):
        """Compatibility method - no driver to close for JSON backend."""
        pass
    
    def query_diseases(self):
        """Get all disease IDs that have predictions.
        
        Returns:
            List of disease IDs
        """
        try:
            disease_dict = self.node_name_dict.get('disease', {})
            disease_ids = list(disease_dict.keys())
            
            # Frontend expects [id, treatable] pairs
            return [[id, True] for id in disease_ids[:100]]  # Limit to first 100 for performance
            
        except Exception as e:
            print(f"Error querying diseases: {e}")
            return []

    def query_drugs(self):
        """Get all drug IDs that have predictions.
        
        Returns:
            List of drug IDs
        """
        try:
            if hasattr(self, 'predictions_df') and not self.predictions_df.empty:
                return self.predictions_df['drug_id'].unique().tolist()
            
            # Fallback to drug_idx2id if predictions not loaded
            return list(self.drug_idx2id.values())[:100]
            
        except Exception as e:
            print(f"Error querying drugs: {e}")
            return []

    def query_predicted_diseases(self, drug_id, top_n):
        """Get predicted disease candidates for a drug.
        
        Args:
            drug_id: Drug ID
            top_n: Number of top predictions to return
            
        Returns:
            List of disease predictions
        """
        try:
            # Store current drug for metapath summary
            self.current_drug = drug_id
            
            if not hasattr(self, 'predictions_df') or self.predictions_df.empty:
                self.diseases = []
                return []
                
            # Filter by drug_id
            df = self.predictions_df[self.predictions_df['drug_id'] == drug_id]
            
            if df.empty:
                self.diseases = []
                return []
                
            # Sort by rank or score
            if 'rank' in df.columns:
                df = df.sort_values('rank')
            elif 'score' in df.columns:
                df = df.sort_values('score', ascending=False)
                
            # Take top N
            df = df.head(top_n)
            
            predictions = []
            for _, row in df.iterrows():
                # Skip rows with NaN disease_id
                if pd.isna(row['disease_id']):
                    continue
                    
                disease_id = str(row['disease_id'])
                if isinstance(row['disease_id'], float) and not pd.isna(row['disease_id']):
                    disease_id = str(int(row['disease_id']))
                
                # Use disease_node_id for attention queries if available
                disease_node_id = disease_id  # default to disease_id
                if 'disease_node_id' in row and pd.notna(row['disease_node_id']):
                    disease_node_id = str(row['disease_node_id'])
                    if isinstance(row['disease_node_id'], float) and not pd.isna(row['disease_node_id']):
                        disease_node_id = str(int(row['disease_node_id']))
                    
                pred = {
                    'id': disease_id,
                    'node_id': disease_node_id,  # Add this for attention queries
                    'name': str(row['disease']) if 'disease' in row else None,
                    'score': float(row['score']),
                    'known': False
                }
                predictions.append(pred)
            
            # Store diseases for metapath summary
            self.diseases = predictions
                
            return predictions
        except Exception as e:
            print(f"Error querying predicted diseases: {e}")
            self.diseases = []
            return []
    
    def query_predicted_drugs(self, disease_id, top_n):
        """Get predicted drug repurposing candidates for a disease.
        
        Args:
            disease_id: Disease ID
            top_n: Number of top predictions to return
            
        Returns:
            List of drug predictions with scores
        """
        try:
            self.current_disease = disease_id
            
            if not hasattr(self, 'predictions_df') or self.predictions_df.empty:
                # Fallback to mock if no predictions loaded
                return self._get_mock_drug_predictions(disease_id, top_n)
                
            # Filter by disease_id
            # Note: disease_id in dataframe might be int or string, ensure consistency
            # Try exact match first
            df = self.predictions_df[self.predictions_df['disease_id'].astype(str) == str(disease_id)]
            if df.empty:
                return self._get_mock_drug_predictions(disease_id, top_n)
                
            # Sort by score
            if 'score' in df.columns:
                df = df.sort_values('score', ascending=False)
            elif 'rank' in df.columns:
                df = df.sort_values('rank')
                
            # Take top N
            df = df.head(top_n)
            
            drugs = []
            for _, row in df.iterrows():
                drug_id = str(row['drug_id'])
                drug_name = None
                
                # Try to get name from node_name_dict
                if 'drug' in self.node_name_dict and drug_id in self.node_name_dict['drug']:
                    drug_name = self.node_name_dict['drug'][drug_id]
                
                drugs.append({
                    'id': drug_id,
                    'score': float(row['score']) if 'score' in row else 0.0,
                    'name': drug_name
                })
                
            self.drugs = drugs
            return drugs
            
        except Exception as e:
            print(f"Error querying predicted drugs: {e}")
            return []

    def _get_mock_drug_predictions(self, disease_id, top_n):
        """Helper to generate mock predictions if real data is missing."""
        drugs = []
        drug_ids = list(self.node_name_dict.get('drug', {}).keys())[:top_n]
        
        for i, drug_id in enumerate(drug_ids):
            score = 1.0 - (i * 0.05)
            drugs.append({
                'id': drug_id,
                'score': max(0.5, score)
            })
        
        if len(drugs) > 6:
            drugs = drugs[:3] + drugs[6:]
            
        self.drugs = drugs
        return drugs
    
    def query_drug_disease_pair(self, disease_id, drug_id):
        """Get prediction score for a specific drug-disease pair.
        
        Args:
            disease_id: Disease ID
            drug_id: Drug ID
            
        Returns:
            Dictionary with score and relation
        """
        try:
            score = 0.0
            if hasattr(self, 'predictions_df') and not self.predictions_df.empty:
                # Look up in predictions df
                mask = (self.predictions_df['drug_id'].astype(str) == str(drug_id)) & \
                       (self.predictions_df['disease_id'].astype(str) == str(disease_id))
                match = self.predictions_df[mask]
                if not match.empty:
                    score = float(match.iloc[0]['score'])
            
            return {
                'score': score,
                'relation': 'rev_indication' # Default relation
            }
        except Exception as e:
            print(f"Error querying drug disease pair: {e}")
            return {'score': 0.0, 'relation': 'unknown'}
    
    def _get_node_edges(self, node_id, node_type, max_edges=50):
        """Get edges for a node (helper function for multi-level tree building)."""
        query_node_id = str(node_id)
        
        # Map disease_id to disease_node_id if applicable
        if node_type == 'disease' and hasattr(self, 'disease_id_map'):
            if query_node_id in self.disease_id_map:
                query_node_id = self.disease_id_map[query_node_id]
        
        all_edges = []
        has_source = hasattr(self, 'attention_by_source') and self.attention_by_source
        has_target = hasattr(self, 'attention_by_target') and self.attention_by_target
        
        # Get edges where this node is the source
        if has_source:
            key_source = (query_node_id, node_type)
            source_edges = self.attention_by_source.get(key_source, [])
            for edge in source_edges[:max_edges]:
                all_edges.append({
                    'nodeId': str(edge['y_id']),
                    'nodeType': edge['y_type'],
                    'score': float(edge.get('layer2_att', 0.5)),
                    'edgeInfo': edge['relation'],
                    'direction': 'out'
                })
        
        # Get edges where this node is the target
        if has_target:
            key_target = (query_node_id, node_type)
            target_edges = self.attention_by_target.get(key_target, [])
            for edge in target_edges[:max_edges]:
                all_edges.append({
                    'nodeId': str(edge['x_id']),
                    'nodeType': edge['x_type'],
                    'score': float(edge.get('layer2_att', 0.5)),
                    'edgeInfo': edge['relation'],
                    'direction': 'in'
                })
        
        # Supplement with subgraph data if available
        if len(all_edges) < 10 and hasattr(self, 'subgraphs') and hasattr(self, 'current_drug'):
            subgraph_key = f"{self.current_drug}_{query_node_id}"
            if subgraph_key in self.subgraphs:
                subgraph = self.subgraphs[subgraph_key]
                for edge in subgraph.get('edges', []):
                    if str(edge['source']) == query_node_id or str(edge['target']) == query_node_id:
                        other_id = str(edge['target']) if str(edge['source']) == query_node_id else str(edge['source'])
                        other_type = 'unknown'
                        for node in subgraph.get('nodes', []):
                            if str(node['id']) == other_id:
                                other_type = node.get('type', 'unknown')
                                break
                        if not any(e['nodeId'] == other_id for e in all_edges):
                            all_edges.append({
                                'nodeId': other_id,
                                'nodeType': other_type,
                                'score': float(edge.get('attention', 0.5)),
                                'edgeInfo': edge.get('relation', 'connected'),
                                'direction': 'out' if str(edge['source']) == query_node_id else 'in'
                            })
        
        return all_edges

    def query_attention(self, node_id, node_type, max_depth=3):
        """Query attention graph for a specific node with multi-level tree.
        
        Args:
            node_id: Node ID
            node_type: Type of node
            max_depth: Maximum depth of the tree (default 3 for 3 layers)
            
        Returns:
            Attention tree structure with multiple levels
        """
        try:
            node_id = str(node_id)
            
            # Map disease_id to disease_node_id if applicable
            query_node_id = node_id
            if node_type == 'disease' and hasattr(self, 'disease_id_map'):
                if node_id in self.disease_id_map:
                    query_node_id = self.disease_id_map[node_id]
            
            # Create root tree structure
            tree = {
                'nodeId': node_id,
                'nodeType': node_type,
                'score': 1.0,
                'edgeInfo': '',
                'children': []
            }
            
            # Build multi-level tree using BFS
            visited = {(node_id, node_type)}
            queue = [(tree, query_node_id, node_type, 0)]  # (parent_node, node_id, node_type, depth)
            
            while queue:
                parent, curr_id, curr_type, depth = queue.pop(0)
                
                if depth >= max_depth:
                    continue
                
                # Get edges for current node
                edges = self._get_node_edges(curr_id, curr_type, max_edges=30 if depth == 0 else 15)
                
                # Sort by score and take top edges
                edges = sorted(edges, key=lambda x: -x['score'])[:20 if depth == 0 else 10]
                
                for edge in edges:
                    child_id = edge['nodeId']
                    child_type = edge['nodeType']
                    
                    # Skip if already visited
                    if (child_id, child_type) in visited:
                        continue
                    
                    visited.add((child_id, child_type))
                    
                    child_node = {
                        'nodeId': child_id,
                        'nodeType': child_type,
                        'score': edge['score'],
                        'edgeInfo': edge['edgeInfo'],
                        'children': []
                    }
                    parent['children'].append(child_node)
                    
                    # Add to queue for further expansion
                    if depth + 1 < max_depth:
                        queue.append((child_node, child_id, child_type, depth + 1))
            
            return tree
        except Exception as e:
            print(f"Error querying attention for {node_id}: {e}")
            return {
                'nodeId': str(node_id),
                'nodeType': node_type,
                'score': 1.0,
                'edgeInfo': '',
                'children': []
            }
    
    def query_attention_old(self, node_id, node_type):
        """Query attention graph for a specific node using real attention data.
        
        Args:
            node_id: Node ID
            node_type: Type of node
            
        Returns:
            Attention tree structure
        """
        try:
            # Normalize node_id to string
            node_id = str(node_id)
            
            # Map disease_id to disease_node_id if applicable
            query_node_id = node_id
            if node_type == 'disease' and hasattr(self, 'disease_id_map'):
                if node_id in self.disease_id_map:
                    query_node_id = self.disease_id_map[node_id]
                    # print(f"Mapped disease_id {node_id} to disease_node_id {query_node_id}")
            
            
            # Create root tree structure
            tree = {
                'nodeId': node_id,
                'nodeType': node_type,
                'score': 1.0,
                'edgeInfo': '',
                'children': []
            }
            
            # Check if we have attention data (source or target)
            has_source = hasattr(self, 'attention_by_source') and self.attention_by_source
            has_target = hasattr(self, 'attention_by_target') and self.attention_by_target
            
            if not has_source and not has_target:
                # print(f"Warning: No attention data available for {node_id}")
                return tree
            
            all_edges = []
            
            # Get edges where this node is the source (x_id)
            key_source = (query_node_id, node_type)
            if has_source:
                source_edges = self.attention_by_source.get(key_source, [])
                for edge in source_edges:
                    all_edges.append({
                        'nodeId': str(edge['y_id']),
                        'nodeType': edge['y_type'],
                        'score': float(edge['layer2_att']),
                        'edgeInfo': edge['relation'],
                        'direction': 'out'
                    })
            
            # Get edges where this node is the target (y_id)
            # Note: attention_by_target keys are (y_id, y_type)
            key_target = (query_node_id, node_type)
            if has_target:
                target_edges = self.attention_by_target.get(key_target, [])
                for edge in target_edges:
                    all_edges.append({
                        'nodeId': str(edge['x_id']),
                        'nodeType': edge['x_type'],
                        'score': float(edge['layer2_att']),
                        'edgeInfo': edge['relation'], # You might want to indicate reverse here if needed
                        'direction': 'in'
                    })
            
            # Special handling for disease nodes: check for protein_disease edges
            # where the disease might be represented as a gene/protein node
            if node_type == 'disease' and has_target:
                key_target_protein = (query_node_id, 'gene/protein')
                target_edges_protein = self.attention_by_target.get(key_target_protein, [])
                for edge in target_edges_protein:
                    if edge['relation'] == 'protein_disease':
                        all_edges.append({
                            'nodeId': str(edge['x_id']),
                            'nodeType': edge['x_type'],
                            'score': float(edge['layer2_att']),
                            'edgeInfo': edge['relation'],
                            'direction': 'in'
                        })
            
            # If disease has few edges, supplement with subgraph data
            if node_type == 'disease' and len(all_edges) < 5 and hasattr(self, 'subgraphs') and hasattr(self, 'current_drug'):
                # Try to get edges from subgraph
                subgraph_key = f"{self.current_drug}_{query_node_id}"
                if subgraph_key in self.subgraphs:
                    subgraph = self.subgraphs[subgraph_key]
                    for edge in subgraph.get('edges', []):
                        # Add edges that connect to/from this disease
                        if edge['source'] == query_node_id or edge['target'] == query_node_id:
                            other_id = edge['target'] if edge['source'] == query_node_id else edge['source']
                            # Find node type from subgraph nodes
                            other_type = 'unknown'
                            for node in subgraph.get('nodes', []):
                                if node['id'] == other_id:
                                    other_type = node['type']
                                    break
                            
                            if other_type != 'unknown':
                                all_edges.append({
                                    'nodeId': str(other_id),
                                    'nodeType': other_type,
                                    'score': float(edge.get('attention', edge.get('layer2_att', 0.5))),
                                    'edgeInfo': edge['relation'],
                                    'direction': 'out' if edge['source'] == query_node_id else 'in'
                                })
            
            if not all_edges:
                # print(f"Warning: No attention edges found for node {node_id} ({node_type})")
                return tree
            
            # Sort edges by score (descending) and take top k
            # MODIFIED: Ensure diversity by taking top k from EACH relation type
            
            # Group by relation
            edges_by_relation = {}
            for edge in all_edges:
                rel = edge['edgeInfo']
                if rel not in edges_by_relation:
                    edges_by_relation[rel] = []
                edges_by_relation[rel].append(edge)
            
            # Select top k from each relation
            selected_edges = []
            top_k_per_rel = 5
            for rel, edges in edges_by_relation.items():
                # Sort this relation's edges
                sorted_rel_edges = sorted(edges, key=lambda x: x['score'], reverse=True)
                selected_edges.extend(sorted_rel_edges[:top_k_per_rel])
            
            # Now sort all selected edges and take top N overall (increased to 20 to allow more context)
            max_children = 20
            sorted_edges = sorted(selected_edges, key=lambda x: x['score'], reverse=True)[:max_children]
            
            # Build children from edges
            for edge in sorted_edges:
                child_id = edge['nodeId']
                child_info = self.node_info.get(child_id, {})
                
                child = {
                    'nodeId': child_id,
                    'nodeType': edge['nodeType'],
                    'score': edge['score'],
                    'edgeInfo': edge['edgeInfo'],
                    'source': child_info.get('source', ''),
                    'children': []
                }
                tree['children'].append(child)
            
            # Add source info to root node as well
            root_info = self.node_info.get(node_id, {})
            tree['source'] = root_info.get('source', '')
            
            return tree
            
        except Exception as e:
            print(f"Error querying attention for {node_id}: {e}")
            import traceback
            traceback.print_exc()
            return {
                'nodeId': node_id,
                'nodeType': node_type,
                'score': 1.0,
                'edgeInfo': '',
                'children': []
            }
    
    def query_attention_pair(self, disease_id, drug_id):
        """Query attention for a disease-drug pair and find connecting metapaths using subgraph data.
        
        Args:
            disease_id: Disease ID (used as part of precomputed_paths key)
            drug_id: Drug ID
            
        Returns:
            Dictionary with attention trees and metapaths
        """
        try:
            # Set current_drug for subgraph lookup in query_attention
            self.current_drug = drug_id
            
            # Get attention trees for both disease and drug (using attention_all.csv)
            attention = {}
            attention[f'disease:{disease_id}'] = self.query_attention(disease_id, 'disease')
            attention[f'drug:{drug_id}'] = self.query_attention(drug_id, 'drug')
            
            # Find metapaths using pre-computed paths if available
            metapaths = []
            
            # Map disease_id to disease_node_id for precomputed paths lookup
            disease_node_id = disease_id
            if hasattr(self, 'disease_id_map') and disease_id in self.disease_id_map:
                disease_node_id = self.disease_id_map[disease_id]
                # print(f"Mapped disease_id {disease_id} to disease_node_id {disease_node_id}")
            
            # Try to load precomputed paths for this drug-disease pair
            # Key format: {drug_id}_{disease_node_id}
            precomputed_key = f"{drug_id}_{disease_node_id}"
            
            # Load precomputed paths if available
            if hasattr(self, 'precomputed_paths') and self.precomputed_paths:
                if precomputed_key in self.precomputed_paths:
                    # The precomputed_paths structure is {key: {metapaths: [...], ...}}
                    path_data = self.precomputed_paths[precomputed_key]
                    if isinstance(path_data, dict) and 'metapaths' in path_data:
                        metapaths = path_data['metapaths']
                    elif isinstance(path_data, list):
                        metapaths = path_data
                    else:
                        metapaths = []
                    # print(f"Loaded {len(metapaths)} precomputed paths for {precomputed_key}")
                else:
                    # Try with string versions of IDs
                    found = False
                    for key in self.precomputed_paths.keys():
                        key_parts = key.split('_')
                        if len(key_parts) >= 2:
                            key_drug = key_parts[0]
                            key_disease = '_'.join(key_parts[1:])
                            if key_drug == str(drug_id) and key_disease == str(disease_id):
                                path_data = self.precomputed_paths[key]
                                if isinstance(path_data, dict) and 'metapaths' in path_data:
                                    metapaths = path_data['metapaths']
                                elif isinstance(path_data, list):
                                    metapaths = path_data
                                found = True
                                break
                    
                    if not found:
                        print(f"No precomputed paths found for {precomputed_key}")
            
            # If no precomputed paths, fall back to attention-based method
            if not metapaths:
                disease_tree = attention[f'disease:{disease_id}']
                drug_tree = attention[f'drug:{drug_id}']
                
                # Extract nodes from disease and drug attention trees
                disease_neighbors = {child['nodeId']: child for child in disease_tree.get('children', [])}
                drug_neighbors = {child['nodeId']: child for child in drug_tree.get('children', [])}
                
                # Find common nodes as bridges
                common_nodes = set(disease_neighbors.keys()) & set(drug_neighbors.keys())
                
                for common_node_id in list(common_nodes)[:10]:  # Limit to 10 metapaths
                    disease_child = disease_neighbors[common_node_id]
                    drug_child = drug_neighbors[common_node_id]
                    
                    metapath = {
                        'nodes': [
                            {'nodeId': drug_id, 'nodeType': 'drug', 'source': ''},
                            {'nodeId': common_node_id, 'nodeType': disease_child['nodeType'], 'source': ''},
                            {'nodeId': disease_id, 'nodeType': 'disease', 'source': ''}
                        ],
                        'edges': [
                            {'edgeInfo': drug_child['edgeInfo'], 'score': drug_child['score']},
                            {'edgeInfo': disease_child['edgeInfo'], 'score': disease_child['score']}
                        ]
                    }
                    metapaths.append(metapath)
                
                # Check for direct connection (Drug -> Disease)
                if str(disease_id) in drug_neighbors:
                    direct_child = drug_neighbors[str(disease_id)]
                    metapath = {
                        'nodes': [
                            {'nodeId': drug_id, 'nodeType': 'drug', 'source': ''},
                            {'nodeId': disease_id, 'nodeType': 'disease', 'source': ''}
                        ],
                        'edges': [
                            {'edgeInfo': direct_child['edgeInfo'], 'score': direct_child['score']}
                        ]
                    }
                    metapaths.append(metapath)

                # Check for reverse connection (Disease -> Drug)
                if str(drug_id) in disease_neighbors:
                     direct_child = disease_neighbors[str(drug_id)]
                     metapath = {
                        'nodes': [
                            {'nodeId': disease_id, 'nodeType': 'disease', 'source': ''},
                            {'nodeId': drug_id, 'nodeType': 'drug', 'source': ''}
                        ],
                        'edges': [
                            {'edgeInfo': direct_child['edgeInfo'], 'score': direct_child['score']}
                        ]
                     }
                     metapaths.append(metapath)
            
            return {
                'attention': attention,
                'metapaths': metapaths
            }
            
        except Exception as e:
            print(f"Error querying attention pair: {e}")
            import traceback
            traceback.print_exc()
            return {
                'attention': {},
                'metapaths': []
            }
    
    def query_metapath_summary(self, top_n):
        """Get summary of metapaths for current disease and drug predictions.
        
        Args:
            top_n: Number of top drugs/diseases to consider
            
        Returns:
            List of metapath summaries
        """
        try:
            # Determine mode and targets based on what's set
            targets = []
            source_id = None
            mode = None # 'drug' (predicting drugs for disease) or 'disease' (predicting diseases for drug)
            
            # Check for disease-to-drug mode first
            if hasattr(self, 'drugs') and self.drugs and hasattr(self, 'current_disease') and self.current_disease:
                targets = self.drugs
                source_id = self.current_disease
                mode = 'drug'
            # Then check for drug-to-disease mode
            elif hasattr(self, 'diseases') and self.diseases and hasattr(self, 'current_drug') and self.current_drug:
                targets = self.diseases
                source_id = self.current_drug
                mode = 'disease'
            else:
                print("Warning: No predictions loaded for metapath summary")
                return []
            
            print(f"Metapath summary mode: {mode}, source: {source_id}, targets: {len(targets)}")
            
            # Dictionary to store counts: key=node_types_tuple, value=dict of counts per target {target_id: count}
            summary_dict = {}
            
            for target in targets[:top_n]:  # Limit to top_n targets
                target_id = target['id']
                
                # Query attention pair - always (disease_id, drug_id) format
                if mode == 'drug':
                    # Disease to Drug mode
                    pair_data = self.query_attention_pair(source_id, target_id)
                else:
                    # Drug to Disease mode
                    pair_data = self.query_attention_pair(target_id, source_id)
                    
                metapaths = pair_data.get('metapaths', [])
                
                for path in metapaths:
                    # Create a signature for the path based on node types
                    node_types = tuple(node['nodeType'] for node in path['nodes'])
                    
                    if node_types not in summary_dict:
                        summary_dict[node_types] = {}
                    
                    if target_id not in summary_dict[node_types]:
                        summary_dict[node_types][target_id] = 0
                    
                    summary_dict[node_types][target_id] += 1
            
            # Convert summary_dict to list format required by frontend
            metapaths_summary = []
            for node_types, counts in summary_dict.items():
                metapaths_summary.append({
                    'nodeTypes': list(node_types),
                    'count': counts,
                    'sum': sum(counts.values())
                })
            
            # Sort by total count
            metapaths_summary.sort(key=lambda x: x['sum'], reverse=True)
            
            print(f"Generated metapath summary with {len(metapaths_summary)} path types")
            
            return metapaths_summary
            
        except Exception as e:
            print(f"Error querying metapath summary: {e}")
            import traceback
            traceback.print_exc()
            return []


def get_db():
    """Get or create database instance for the current request context."""
    if 'db' not in g:
        # Use JSON database instead of Neo4j
        db = JsonDatabase(
            server=current_app.config.get('GNN', 'attention'),
            data_folder=current_app.config.get('DATA_FOLDER', './data')
        )
        db.create_session()
        g.db = db
    return g.db
