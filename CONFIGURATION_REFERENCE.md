# ⚙️ Configuration Reference

This document describes all configurable parameters in the TxGNN Drug Repurposing pipeline.

---

## 1. TxGNN Prediction Script

**File:** `txgnn_company_repurpose_end2end.py`

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DATA_DIR` | `./data` | Path to KG data files |
| `MODEL_DIR` | `./model_ckpt` | Path to trained model |
| `OUTPUT_DIR` | `./repurpose_out` | Output directory |

### Script Parameters

```python
# In txgnn_company_repurpose_end2end.py

TOP_N_DISEASES = 50          # Number of diseases to predict per drug
RELATION_TYPE = 'indication' # Prediction type: 'indication' or 'contraindication'
RANDOM_SEED = 42             # For reproducibility
```

### Input Files Required

| File | Location | Description |
|------|----------|-------------|
| `node.csv` | `data/` | All nodes (129,375 total) |
| `kg.csv` | `data/` | Knowledge graph edges |
| `model.pt` | `model_ckpt/` | Trained TxGNN weights |
| `node_emb.pkl` | `model_ckpt/` | Node embeddings (512-dim) |
| `config.pkl` | `model_ckpt/` | Model configuration |
| `present_drugs.csv` | `repurpose_out/` | List of company drugs |
| `kg_drug_catalog.csv` | `repurpose_out/` | Drug ID mapping |

---

## 2. Data Processing Script

**File:** `process_all_drugs.py`

### Command Line Arguments

```bash
python process_all_drugs.py [OPTIONS]
```

| Argument | Default | Description |
|----------|---------|-------------|
| `--data_dir` | `./data` | KG data directory |
| `--predictions_dir` | `./repurpose_out` | Predictions input |
| `--output_dir` | `./drugExplorer/data` | Output directory |
| `--ckpt_dir` | `./model_ckpt` | Model checkpoint |
| `--top_diseases` | `50` | Max diseases per drug |
| `--beam_width` | `1000` | Beam search width |
| `--top_k_paths` | `10` | Paths per drug-disease |

### Output Files Generated

| File | Description |
|------|-------------|
| `your_predictions.csv` | Combined predictions |
| `attention_all.csv` | Attention scores |
| `subgraph_*.json` | Subgraphs |
| `disease_info.json` | Disease metadata |
| `drug_info.json` | Drug metadata |
| `disease_tsne.json` | Disease embeddings |
| `best_paths.json` | Top paths |
| `processed_drugs.json` | Processing status |

---

## 3. Deep Path Generator

**File:** `generate_all_deep_paths.py`

### Command Line Arguments

```bash
python generate_all_deep_paths.py [OPTIONS]
```

| Argument | Default | Description |
|----------|---------|-------------|
| `--data_dir` | `./data` | KG data directory |
| `--model_dir` | `./model_ckpt` | Model checkpoint |
| `--output_dir` | `./drugExplorer/data` | Output directory |
| `--max_depth` | `5` | Maximum path hops |
| `--max_paths` | `2000` | Max paths per drug |
| `--min_attention` | `0.4` | Minimum attention threshold |

### Performance Tuning

```python
# In generate_all_deep_paths.py

BFS_MAX_QUEUE = 100000   # Max BFS queue size (memory)
BATCH_SIZE = 1000        # Paths processed per batch
NUM_WORKERS = 4          # Parallel workers (if enabled)
```

### Output Files

| File Pattern | Description |
|--------------|-------------|
| `{drug_name}_scored_paths.json` | Paths per drug |
| `deep_paths_summary.json` | Processing summary |

---

## 4. Flask Backend Configuration

**File:** `drugExplorer/application.py`

### Server Settings

```python
# In application.py

HOST = '0.0.0.0'         # Bind address
PORT = 8002              # Server port
DEBUG = True             # Debug mode (disable in production)
USE_RELOADER = False     # Disable to prevent double-init
```

### API Cache Settings

**File:** `drugExplorer/api.py`

```python
# Cache configuration
_cache_max_size = 500    # Max cached responses
_cache_ttl = 3600        # Cache TTL in seconds (not implemented)
```

### Database Settings

**File:** `drugExplorer/database_json.py`

```python
# In JsonDatabase class

DATA_FOLDER = 'data'          # Data subfolder path
PRELOAD_ALL = True            # Preload all data at startup
CACHE_ENABLED = True          # Enable internal caching
```

---

## 5. React Frontend Configuration

**File:** `drugExplorer/package.json`

```json
{
  "proxy": "http://localhost:8002",
  "homepage": ".",
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build"
  }
}
```

### Development Settings

**File:** `drugExplorer/.env` (create if needed)

```bash
# React development settings
PORT=3000                     # Dev server port
REACT_APP_API_URL=http://localhost:8002
BROWSER=none                  # Don't auto-open browser
```

### Build Optimization

**File:** `drugExplorer/tsconfig.json`

```json
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "es6"],
    "strict": true,
    "noUnusedLocals": false,    // Allow unused vars
    "skipLibCheck": true
  }
}
```

---

## 6. Data Service Configuration

**File:** `drugExplorer/src/stores/DataService.ts`

### Cache Settings

```typescript
// Client-side cache configuration
const CACHE_ENABLED = true;
const PRELOAD_ENABLED = true;
const MAX_CACHE_SIZE = 1000;
const PRELOAD_BATCH_SIZE = 5;
```

### API Endpoints

```typescript
const API_BASE = '/api';

const ENDPOINTS = {
  drugs: '/drugs',
  diseases: '/diseases',
  predictions: '/disease_predictions',
  attention: '/attention',
  attention_pair: '/attention_pair',
  subgraph: '/subgraph',
  embeddings: '/disease_embeddings',
  best_path: '/best_path',
  all_paths: '/all_paths',
};
```

---

## 7. Visualization Component Settings

### AllPaths Tab

**File:** `drugExplorer/src/components/TabContainer/AllPaths.tsx`

```typescript
// Display settings
const DEFAULT_MIN_HOPS = 2;
const DEFAULT_MAX_HOPS = 5;
const MAX_DISPLAYED_PATHS = 50;
const SORT_OPTIONS = ['combined_score', 'avg_attention', 'hops'];
```

### SubGraph Visualization

**File:** `drugExplorer/src/components/TabContainer/V1SubGraph.tsx`

```typescript
// D3 force simulation settings
const SIMULATION_SETTINGS = {
  charge_strength: -300,     // Node repulsion
  link_distance: 80,         // Edge length
  collision_radius: 30,      // Node collision
  alpha_decay: 0.02,         // Simulation cooling
};
```

### Color Schemes

**File:** `drugExplorer/src/helpers/index.ts`

```typescript
// Node type colors
export const NODE_COLORS = {
  drug: '#e74c3c',
  disease: '#3498db',
  gene: '#2ecc71',
  protein: '#9b59b6',
  pathway: '#f39c12',
  biological_process: '#1abc9c',
  molecular_function: '#34495e',
  cellular_component: '#e67e22',
  anatomy: '#95a5a6',
  effect_phenotype: '#d35400',
};

// Attention score colors
export const ATTENTION_COLORS = {
  high: '#28a745',    // >= 0.7
  medium: '#f0ad4e',  // >= 0.5
  low: '#d9534f',     // < 0.5
};
```

---

## 8. Full Pipeline Script

**File:** `run_full_pipeline.sh`

```bash
#!/bin/bash
set -e

# Configuration
export DATA_DIR="./data"
export MODEL_DIR="./model_ckpt"
export OUTPUT_DIR="./repurpose_out"
export DRUGEXPLORER_DIR="./drugExplorer"

# Steps
echo "Step 1: Running TxGNN predictions..."
python txgnn_company_repurpose_end2end.py

echo "Step 2: Processing data..."
python process_all_drugs.py

echo "Step 3: Generating deep paths..."
python generate_all_deep_paths.py

echo "Step 4: Building frontend..."
cd $DRUGEXPLORER_DIR
npm run build

echo "Step 5: Updating demo folder..."
cd ..
./update_demo.sh

echo "✅ Pipeline complete!"
```

---

## Best Practices

### Production Settings

```python
# application.py - Production mode
DEBUG = False
USE_RELOADER = False

# Run with gunicorn instead
# gunicorn -w 4 -b 0.0.0.0:8002 application:app
```

### Memory Optimization

```python
# For limited memory environments

# In generate_all_deep_paths.py
BFS_MAX_QUEUE = 50000     # Reduce queue size
BATCH_SIZE = 500          # Smaller batches

# In database_json.py
PRELOAD_ALL = False       # Lazy loading
```

### Debug Logging

```python
# Enable verbose logging
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

*Last Updated: December 2025*

