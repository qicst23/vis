#!/usr/bin/env python3
"""
Generate Path Explanation Documents for All Drugs

This script reads the scored paths JSON files and generates detailed
Markdown explanation documents for each drug, similar to INEBILIZUMAB_PATH_ANALYSIS.md

Usage:
    python generate_path_explanations.py [--data_dir ./drugExplorer/data] [--output_dir ./drugExplorer/docs]
"""

import os
import json
import argparse
import glob
from datetime import datetime
from typing import Dict, List, Any, Optional


def load_scored_paths(filepath: str) -> Optional[Dict[str, Any]]:
    """Load scored paths from JSON file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None


def get_attention_rating(score: float) -> str:
    """Convert attention score to star rating."""
    if score >= 0.70:
        return "⭐⭐⭐⭐⭐ Very High"
    elif score >= 0.60:
        return "⭐⭐⭐⭐ High"
    elif score >= 0.50:
        return "⭐⭐⭐ Medium"
    elif score >= 0.40:
        return "⭐⭐ Low"
    else:
        return "⭐ Very Low"


def format_path_visualization(path: Dict[str, Any]) -> str:
    """Format a path as a visual representation."""
    nodes = path.get('nodes', [])
    attention_scores = path.get('attention_scores', [])
    
    parts = []
    for i, node in enumerate(nodes):
        name = node.get('name', 'Unknown')
        # Truncate long names
        if len(name) > 25:
            name = name[:22] + "..."
        parts.append(f"[{name}]")
        
        if i < len(attention_scores) and attention_scores[i] is not None:
            parts.append(f" --({attention_scores[i]:.3f})--> ")
    
    return "".join(parts[:-1])  # Remove trailing arrow


def interpret_path(path: Dict[str, Any], drug_name: str) -> str:
    """Generate biological interpretation for a path."""
    nodes = path.get('nodes', [])
    if len(nodes) < 2:
        return "Path too short for interpretation."
    
    # Get node types
    node_types = [n.get('type', 'unknown') for n in nodes]
    disease_name = nodes[-1].get('name', 'Unknown Disease')
    
    # Determine path type and generate interpretation
    if len(nodes) == 2:
        # Direct drug -> disease
        return f"**Direct prediction**: TxGNN predicts {drug_name} may treat {disease_name} based on embedding similarity."
    
    elif len(nodes) == 3:
        intermediate = nodes[1]
        int_name = intermediate.get('name', 'Unknown')
        int_type = intermediate.get('type', 'unknown')
        
        if 'drug' in int_type.lower():
            return f"**Drug similarity path**: {drug_name} is similar to {int_name}, which is associated with {disease_name}. This suggests shared therapeutic mechanisms."
        elif 'gene' in int_type.lower() or 'protein' in int_type.lower():
            return f"**Target-based path**: {drug_name} targets {int_name}, which is implicated in {disease_name}. This represents a direct mechanistic link."
        elif 'pathway' in int_type.lower():
            return f"**Pathway-mediated**: {drug_name} affects the {int_name} pathway, which is relevant to {disease_name}."
        elif 'biological_process' in int_type.lower():
            return f"**Biological process link**: {drug_name} modulates {int_name}, a process involved in {disease_name}."
        else:
            return f"**Indirect connection**: {drug_name} connects to {disease_name} via {int_name} ({int_type})."
    
    else:
        # Longer paths (4+ nodes)
        intermediates = [n.get('name', '?') for n in nodes[1:-1]]
        return f"**Multi-hop path**: {drug_name} connects to {disease_name} through {len(intermediates)} intermediate nodes: {' → '.join(intermediates)}. This represents a complex biological relationship requiring further validation."


def categorize_paths_by_type(paths: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Categorize paths by intermediate node type."""
    categories = {
        'drug_similarity': [],
        'protein_target': [],
        'pathway': [],
        'biological_process': [],
        'other': []
    }
    
    for path in paths:
        nodes = path.get('nodes', [])
        if len(nodes) < 3:
            categories['other'].append(path)
            continue
        
        # Check intermediate node type
        intermediate_type = nodes[1].get('type', '').lower()
        
        if 'drug' in intermediate_type:
            categories['drug_similarity'].append(path)
        elif 'gene' in intermediate_type or 'protein' in intermediate_type:
            categories['protein_target'].append(path)
        elif 'pathway' in intermediate_type:
            categories['pathway'].append(path)
        elif 'biological' in intermediate_type or 'process' in intermediate_type:
            categories['biological_process'].append(path)
        else:
            categories['other'].append(path)
    
    return categories


def generate_markdown(data: Dict[str, Any], drug_name: str) -> str:
    """Generate complete markdown document for a drug."""
    
    drug_info = data.get('drug', {})
    # Try multiple keys for paths (different file formats)
    paths = data.get('paths', [])
    if not paths:
        paths = data.get('global_top_100', [])
    if not paths:
        # Flatten top_paths_per_disease if available
        top_per_disease = data.get('top_paths_per_disease', {})
        if top_per_disease:
            paths = []
            for disease_paths in top_per_disease.values():
                if isinstance(disease_paths, list):
                    paths.extend(disease_paths)
    
    statistics = data.get('statistics', {})
    paths_by_hops = data.get('paths_by_hops', {})
    
    # Get unique diseases
    unique_diseases = set()
    for p in paths:
        nodes = p.get('nodes', [])
        if nodes:
            unique_diseases.add(nodes[-1].get('name', 'Unknown'))
    
    # Sort paths by combined score
    sorted_paths = sorted(paths, key=lambda x: x.get('combined_score', 0), reverse=True)
    top_20_paths = sorted_paths[:20]
    
    # Categorize paths
    categories = categorize_paths_by_type(paths)
    
    # Build markdown
    md = []
    
    # Header
    md.append(f"# 🔬 {drug_name} Path Analysis Report")
    md.append("")
    md.append(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    md.append("")
    
    # Drug Profile
    md.append("## 1. Drug Profile")
    md.append("")
    md.append(f"| Property | Value |")
    md.append(f"|----------|-------|")
    md.append(f"| **Drug ID** | {drug_info.get('id', 'N/A')} |")
    md.append(f"| **Drug Name** | {drug_info.get('name', drug_name)} |")
    md.append(f"| **Type** | {drug_info.get('type', 'drug')} |")
    md.append("")
    
    # Path Statistics
    md.append("## 2. Path Statistics")
    md.append("")
    md.append(f"| Metric | Value |")
    md.append(f"|--------|-------|")
    md.append(f"| **Total Paths** | {len(paths):,} |")
    md.append(f"| **Unique Diseases** | {len(unique_diseases):,} |")
    md.append(f"| **Mean Attention** | {statistics.get('mean_attention', 0):.4f} |")
    md.append(f"| **Std Attention** | {statistics.get('std_attention', 0):.4f} |")
    md.append(f"| **Min Attention** | {statistics.get('min_attention', 0):.4f} |")
    md.append(f"| **Max Attention** | {statistics.get('max_attention', 0):.4f} |")
    md.append("")
    
    # Paths by hop count
    md.append("### Paths by Hop Count")
    md.append("")
    md.append("| Hops | Count |")
    md.append("|------|-------|")
    for hop, count in sorted(paths_by_hops.items()):
        md.append(f"| {hop} | {count:,} |")
    md.append("")
    
    # Path Type Summary
    md.append("## 3. Path Type Summary")
    md.append("")
    md.append("| Path Type | Count | Description |")
    md.append("|-----------|-------|-------------|")
    md.append(f"| Drug Similarity | {len(categories['drug_similarity']):,} | Paths through similar drugs |")
    md.append(f"| Protein Target | {len(categories['protein_target']):,} | Paths through protein targets |")
    md.append(f"| Pathway | {len(categories['pathway']):,} | Paths through biological pathways |")
    md.append(f"| Biological Process | {len(categories['biological_process']):,} | Paths through biological processes |")
    md.append(f"| Other | {len(categories['other']):,} | Other connection types |")
    md.append("")
    
    # Top Similar Drugs (if any)
    if categories['drug_similarity']:
        md.append("### Key Similar Drugs")
        md.append("")
        similar_drugs = {}
        for p in categories['drug_similarity']:
            nodes = p.get('nodes', [])
            if len(nodes) >= 2:
                drug_node = nodes[1].get('name', 'Unknown')
                att = p.get('attention_scores', [0])[0] or 0
                if drug_node not in similar_drugs or att > similar_drugs[drug_node]:
                    similar_drugs[drug_node] = att
        
        md.append("| Similar Drug | Max Attention | # Diseases |")
        md.append("|--------------|---------------|------------|")
        for drug, att in sorted(similar_drugs.items(), key=lambda x: x[1], reverse=True)[:10]:
            count = len([p for p in categories['drug_similarity'] if len(p.get('nodes', [])) >= 2 and p['nodes'][1].get('name') == drug])
            md.append(f"| {drug} | {att:.4f} | {count} |")
        md.append("")
    
    # Top 20 Paths
    md.append("## 4. Top 20 Paths (by Combined Score)")
    md.append("")
    
    for i, path in enumerate(top_20_paths, 1):
        nodes = path.get('nodes', [])
        disease_name = nodes[-1].get('name', 'Unknown') if nodes else 'Unknown'
        
        md.append(f"### Path #{i}: {disease_name}")
        md.append("")
        
        # Path visualization
        md.append("**Path:**")
        md.append("```")
        md.append(format_path_visualization(path))
        md.append("```")
        md.append("")
        
        # Path details
        md.append("| Metric | Value |")
        md.append("|--------|-------|")
        md.append(f"| Hops | {path.get('hops', 'N/A')} |")
        md.append(f"| Avg Attention | {path.get('avg_attention', 0):.4f} |")
        md.append(f"| Combined Score | {path.get('combined_score', 0):.4f} |")
        md.append(f"| Confidence | {get_attention_rating(path.get('avg_attention', 0))} |")
        md.append("")
        
        # Node types
        md.append("**Node Types:** " + " → ".join([f"`{n.get('type', 'unknown')}`" for n in nodes]))
        md.append("")
        
        # Interpretation
        md.append("**Interpretation:**")
        md.append("")
        md.append(interpret_path(path, drug_name))
        md.append("")
        md.append("---")
        md.append("")
    
    # Interpretation Guidelines
    md.append("## 5. Interpretation Guidelines")
    md.append("")
    md.append("### Attention Score Scale")
    md.append("")
    md.append("| Score Range | Confidence | Interpretation |")
    md.append("|-------------|------------|----------------|")
    md.append("| ≥ 0.70 | ⭐⭐⭐⭐⭐ Very High | Strong biological relationship |")
    md.append("| 0.60 - 0.70 | ⭐⭐⭐⭐ High | Good evidence for connection |")
    md.append("| 0.50 - 0.60 | ⭐⭐⭐ Medium | Moderate support |")
    md.append("| 0.40 - 0.50 | ⭐⭐ Low | Weak connection |")
    md.append("| < 0.40 | ⭐ Very Low | Speculative |")
    md.append("")
    
    md.append("### How to Use This Report")
    md.append("")
    md.append("1. **Prioritize high-scoring paths**: Focus on paths with combined scores > 0.45")
    md.append("2. **Validate intermediate nodes**: Cross-reference proteins/drugs with literature")
    md.append("3. **Consider path length**: Shorter paths (2-3 hops) are generally more reliable")
    md.append("4. **Check for known associations**: Some paths may represent known indications")
    md.append("")
    
    md.append("---")
    md.append("")
    md.append(f"*Report generated by TxGNN Path Analysis Pipeline*")
    
    return "\n".join(md)


def main():
    parser = argparse.ArgumentParser(description="Generate path explanation documents for all drugs")
    parser.add_argument('--data_dir', default='./drugExplorer/data', help='Directory containing scored paths JSON files')
    parser.add_argument('--output_dir', default='./drugExplorer/docs', help='Output directory for markdown files')
    args = parser.parse_args()
    
    print("=" * 80)
    print("GENERATING PATH EXPLANATION DOCUMENTS")
    print("=" * 80)
    print(f"Data directory: {args.data_dir}")
    print(f"Output directory: {args.output_dir}")
    print()
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Find all scored paths files
    pattern = os.path.join(args.data_dir, '*_scored_paths.json')
    files = glob.glob(pattern)
    
    if not files:
        print(f"No scored paths files found matching: {pattern}")
        return
    
    print(f"Found {len(files)} drugs to process")
    print()
    
    generated = []
    errors = []
    
    for filepath in sorted(files):
        filename = os.path.basename(filepath)
        drug_key = filename.replace('_scored_paths.json', '')
        drug_name = drug_key.replace('_', ' ').title()
        
        print(f"Processing {drug_name}...", end=" ")
        
        data = load_scored_paths(filepath)
        if data is None:
            errors.append(drug_name)
            print("ERROR")
            continue
        
        # Update drug name from data if available
        if 'drug' in data and 'name' in data['drug']:
            drug_name = data['drug']['name']
        
        # Generate markdown
        markdown = generate_markdown(data, drug_name)
        
        # Write to file
        output_filename = f"{drug_key.upper()}_PATH_ANALYSIS.md"
        output_path = os.path.join(args.output_dir, output_filename)
        
        with open(output_path, 'w') as f:
            f.write(markdown)
        
        generated.append((drug_name, output_path))
        print(f"OK -> {output_filename}")
    
    # Summary
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Successfully generated: {len(generated)} documents")
    if errors:
        print(f"Errors: {len(errors)} - {', '.join(errors)}")
    print()
    print("Generated files:")
    for drug_name, path in generated:
        print(f"  - {drug_name}: {path}")
    print()
    
    # Also copy to demo folder
    demo_dir = './demo'
    if os.path.exists(demo_dir):
        print("Copying to demo folder...")
        for drug_name, src_path in generated:
            dst_path = os.path.join(demo_dir, os.path.basename(src_path))
            with open(src_path, 'r') as f:
                content = f.read()
            with open(dst_path, 'w') as f:
                f.write(content)
        print(f"Copied {len(generated)} files to {demo_dir}/")


if __name__ == '__main__':
    main()

