# 🚀 TxGNN Drug Repurposing: Complete Implementation Guide

## Overview

This guide provides step-by-step instructions with **exact Python and npm commands** for implementing the TxGNN drug repurposing pipeline, from running the model to visualizing results.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        PIPELINE OVERVIEW                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   Step 1: TxGNN Predictions ──► Step 2: Data Processing ──► Step 3: Paths   │
│                                                                              │
│              ▼                           ▼                        ▼          │
│                                                                              │
│   Step 4: Build Frontend ──────────────► Step 5: Start Server & Test        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Prerequisites

### System Requirements
```bash
# Check Python version (requires 3.8+)
python3 --version

# Check Node.js version (requires 14+)
node --version
npm --version

# Check available disk space (need 10GB+)
df -h
```

### Directory Structure
```bash
# Your project should have this structure
txgnn/
├── data/                    # Knowledge graph data
│   ├── node.csv             # Node definitions
│   └── kg.csv               # Edge definitions
├── model_ckpt/              # Trained model
│   ├── model.pt
│   └── node_emb.pkl
├── repurpose_out/           # TxGNN outputs
└── drugExplorer/            # Visualization app
```

---

## Step 1: Run TxGNN Predictions

### 1.1 Setup Python Environment

```bash
# Navigate to project root
cd /home/nchen10/cursor_prjs/txgnn

# Create virtual environment (if not exists)
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install torch pandas numpy scikit-learn
pip install TxGNN
```

### 1.2 Run TxGNN for a Single Drug (Inebilizumab Test)

```bash
# Run predictions for Inebilizumab with top 100 diseases
python txgnn_company_repurpose_end2end.py \
    --data_dir ./data \
    --ckpt_dir ./model_ckpt \
    --out_dir ./repurpose_out \
    --device cuda:0 \
    --company custom \
    --custom_drug_list ./test_drug.txt \
    --relation indication \
    --fuzzy_match
```

**Create test_drug.txt first:**
```bash
echo "inebilizumab" > test_drug.txt
```

### 1.3 Run TxGNN for All Company Drugs

```bash
# Run for all Amgen + Horizon drugs
python txgnn_company_repurpose_end2end.py \
    --data_dir ./data \
    --ckpt_dir ./model_ckpt \
    --out_dir ./repurpose_out \
    --device cuda:0 \
    --company both \
    --relation indication \
    --fuzzy_match
```

### Expected Output Files
```
repurpose_out/
├── per_drug/
│   ├── inebilizumab_repurposing.csv   # Per-drug predictions
│   ├── adalimumab_repurposing.csv
│   └── ...
├── summary_report.csv                  # Processing summary
├── present_drugs.csv                   # Resolved drugs
└── missing_drugs.csv                   # Unresolved drugs
```

---

## Step 2: Process Data for Visualization

### 2.1 Run Data Processing Script

```bash
# Activate environment
cd /home/nchen10/cursor_prjs/txgnn
source .venv/bin/activate

# Process all predictions for visualization
python process_all_drugs.py \
    --data_dir ./data \
    --predictions_dir ./repurpose_out \
    --output_dir ./drugExplorer/data \
    --ckpt_dir ./model_ckpt \
    --top_diseases 100
```

### 2.2 Alternative: Simplified Processing

If `process_all_drugs.py` doesn't exist, use this consolidated command:

```bash
# Copy prediction data to visualization folder
python -c "
import os
import shutil
import pandas as pd

# Copy predictions CSV
src = 'data/your_predictions.csv'
dst = 'drugExplorer/data/your_predictions.csv'
if os.path.exists(src):
    shutil.copy(src, dst)
    print(f'Copied {src} to {dst}')

# Verify data
df = pd.read_csv(dst)
print(f'Total predictions: {len(df)}')
print(f'Drugs: {df[\"drug_id\"].nunique()}')
print(f'Sample:')
print(df.head())
"
```

### Expected Output Files
```
drugExplorer/data/
├── your_predictions.csv        # Combined predictions
├── attention_all.csv           # Attention scores
├── disease_info.json           # Disease metadata
├── drug_info.json              # Drug metadata
└── processed_drugs.json        # Processing status
```

---

## Step 3: Generate Deep Paths (2-5 hops)

### 3.1 Run Deep Path Generator

```bash
# Activate environment
cd /home/nchen10/cursor_prjs/txgnn
source .venv/bin/activate

# Generate deep paths for all processed drugs
python generate_all_deep_paths.py \
    --data_dir ./data \
    --model_dir ./model_ckpt \
    --output_dir ./drugExplorer/data \
    --max_depth 5 \
    --max_paths 2000
```

### 3.2 Generate Paths for Single Drug (Test)

```bash
# For Inebilizumab only
python generate_all_deep_paths.py \
    --data_dir ./data \
    --model_dir ./model_ckpt \
    --output_dir ./drugExplorer/data \
    --drug_filter "inebilizumab" \
    --max_depth 5 \
    --max_paths 2000
```

### Expected Output Files
```
drugExplorer/data/
├── inebilizumab_scored_paths.json   # Paths for Inebilizumab
├── adalimumab_scored_paths.json     # Paths for other drugs...
├── ...
└── deep_paths_summary.json          # Summary statistics
```

---

## Step 4: Build Frontend

### 4.1 Install Node.js Dependencies

```bash
# Navigate to drugExplorer
cd /home/nchen10/cursor_prjs/txgnn/drugExplorer

# Install dependencies
npm install

# Check for errors
npm audit fix --force  # Optional: fix vulnerabilities
```

### 4.2 Build Production Bundle

```bash
# Build optimized frontend
npm run build

# Verify build
ls -la build/
```

### Expected Output
```
drugExplorer/build/
├── index.html
├── static/
│   ├── css/
│   └── js/
└── asset-manifest.json
```

### 4.3 (Optional) Development Mode

```bash
# Start dev server with hot reload (for development)
npm start

# This opens http://localhost:3000
# Note: API calls will proxy to backend on port 8002
```

---

## Step 5: Start Flask Server & Test

### 5.1 Setup Backend Environment

```bash
# Navigate to drugExplorer
cd /home/nchen10/cursor_prjs/txgnn/drugExplorer

# Create backend virtual environment
python3 -m venv .venv

# Activate
source .venv/bin/activate

# Install requirements
pip install flask flask-cors pandas numpy scikit-learn
```

### 5.2 Start the Server

```bash
# Start Flask server
python application.py
```

**Expected Output:**
```
 * Serving Flask app "application"
 * Running on http://0.0.0.0:8002/ (Press CTRL+C to quit)
Loading database...
Database loaded successfully.
```

### 5.3 Verify API Endpoints

```bash
# In a new terminal, test the API
curl http://localhost:8002/api/drugs
curl http://localhost:8002/api/diseases
curl "http://localhost:8002/api/disease_predictions?drug_id=DB12530&top_n=10"
```

### 5.4 Access the Dashboard

Open your browser:
```
http://localhost:8002
```

---

## Complete Pipeline Script

### run_pipeline.sh

```bash
#!/bin/bash
set -e

echo "=========================================="
echo "TxGNN Drug Repurposing Pipeline"
echo "=========================================="

# Configuration
PROJECT_ROOT="/home/nchen10/cursor_prjs/txgnn"
cd $PROJECT_ROOT

# Step 1: TxGNN Predictions
echo ""
echo ">>> Step 1: Running TxGNN predictions..."
source .venv/bin/activate

# Create test drug file
echo "inebilizumab" > test_drug.txt

python txgnn_company_repurpose_end2end.py \
    --data_dir ./data \
    --ckpt_dir ./model_ckpt \
    --out_dir ./repurpose_out \
    --device cuda:0 \
    --company custom \
    --custom_drug_list ./test_drug.txt \
    --relation indication \
    --fuzzy_match

echo "✅ Step 1 complete"

# Step 2: Process Data
echo ""
echo ">>> Step 2: Processing data for visualization..."
python process_all_drugs.py \
    --data_dir ./data \
    --predictions_dir ./repurpose_out \
    --output_dir ./drugExplorer/data \
    --ckpt_dir ./model_ckpt \
    --top_diseases 100

echo "✅ Step 2 complete"

# Step 3: Generate Deep Paths
echo ""
echo ">>> Step 3: Generating deep paths..."
python generate_all_deep_paths.py \
    --data_dir ./data \
    --model_dir ./model_ckpt \
    --output_dir ./drugExplorer/data \
    --max_depth 5 \
    --max_paths 2000

echo "✅ Step 3 complete"

# Step 4: Build Frontend
echo ""
echo ">>> Step 4: Building frontend..."
cd drugExplorer
npm install
npm run build

echo "✅ Step 4 complete"

# Step 5: Start Server
echo ""
echo ">>> Step 5: Starting server..."
source .venv/bin/activate
echo "Starting Flask server on http://localhost:8002"
python application.py
```

### Make it executable:
```bash
chmod +x run_pipeline.sh
./run_pipeline.sh
```

---

## Quick Test: Inebilizumab Only

### test_inebilizumab.sh

```bash
#!/bin/bash
set -e

PROJECT_ROOT="/home/nchen10/cursor_prjs/txgnn"
cd $PROJECT_ROOT

echo "=========================================="
echo "Testing Pipeline with Inebilizumab"
echo "=========================================="

# Activate environment
source .venv/bin/activate

# Step 1: Create test drug file
echo "inebilizumab" > test_drug.txt

# Step 2: Run TxGNN for Inebilizumab
echo ">>> Running TxGNN for Inebilizumab (top 100 diseases)..."
python txgnn_company_repurpose_end2end.py \
    --data_dir ./data \
    --ckpt_dir ./model_ckpt \
    --out_dir ./repurpose_out \
    --device cuda:0 \
    --company custom \
    --custom_drug_list ./test_drug.txt \
    --relation indication \
    --fuzzy_match

# Step 3: Check output
echo ""
echo ">>> Checking predictions..."
head -20 repurpose_out/per_drug/inebilizumab_repurposing.csv

# Step 4: Copy to visualization
echo ""
echo ">>> Copying to visualization folder..."
cp data/your_predictions.csv drugExplorer/data/

# Step 5: Generate deep paths
echo ""
echo ">>> Generating deep paths for Inebilizumab..."
python generate_all_deep_paths.py \
    --data_dir ./data \
    --model_dir ./model_ckpt \
    --output_dir ./drugExplorer/data \
    --drug_filter "inebilizumab" \
    --max_depth 5

# Step 6: Start server
echo ""
echo ">>> Starting server..."
cd drugExplorer
source .venv/bin/activate
python application.py
```

---

## Troubleshooting

### Common Issues & Solutions

| Issue | Command to Fix |
|-------|----------------|
| Port 8002 in use | `lsof -ti:8002 \| xargs kill -9` |
| Missing Python packages | `pip install -r requirements.txt` |
| npm install fails | `rm -rf node_modules && npm install` |
| No predictions | Check `repurpose_out/summary_report.csv` |
| Wrong drug | Verify `present_drugs.csv` |

### Debug Commands

```bash
# Check if server is running
curl -s http://localhost:8002/api/test

# Check available drugs
curl -s http://localhost:8002/api/drugs | python -m json.tool

# Check predictions for a drug
curl -s "http://localhost:8002/api/disease_predictions?drug_id=DB12530" | python -m json.tool | head -50

# Check path data
ls -la drugExplorer/data/*_scored_paths.json

# View prediction file
head -20 drugExplorer/data/your_predictions.csv
```

---

## Summary of Commands

| Step | Command |
|------|---------|
| **1. TxGNN Predictions** | `python txgnn_company_repurpose_end2end.py --data_dir ./data --ckpt_dir ./model_ckpt --out_dir ./repurpose_out --company both --relation indication --fuzzy_match` |
| **2. Process Data** | `python process_all_drugs.py --data_dir ./data --output_dir ./drugExplorer/data --top_diseases 100` |
| **3. Generate Paths** | `python generate_all_deep_paths.py --data_dir ./data --output_dir ./drugExplorer/data --max_depth 5` |
| **4. Build Frontend** | `cd drugExplorer && npm install && npm run build` |
| **5. Start Server** | `cd drugExplorer && python application.py` |
| **6. Access Dashboard** | Open `http://localhost:8002` |

---

*Document Version: 2.0*
*Last Updated: December 2025*
