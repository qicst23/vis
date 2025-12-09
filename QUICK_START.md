# ⚡ Quick Start Guide

This is a condensed version of the implementation guide. For full details, see `IMPLEMENTATION_GUIDE.md`.

---

## One-Command Pipeline

```bash
# Run the full pipeline
./run_full_pipeline.sh
```

---

## Step-by-Step Commands

### 1️⃣ Run TxGNN Predictions
```bash
source .venv/bin/activate
python txgnn_company_repurpose_end2end.py
```
**Output:** `repurpose_out/predictions_all.csv`

### 2️⃣ Process Data for Visualization
```bash
python process_all_drugs.py
```
**Output:** `drugExplorer/data/*.json`

### 3️⃣ Generate Deep Paths
```bash
python generate_all_deep_paths.py
```
**Output:** `drugExplorer/data/*_scored_paths.json`

### 4️⃣ Build Frontend
```bash
cd drugExplorer
npm install
npm run build
```
**Output:** `drugExplorer/build/`

### 5️⃣ Start Server
```bash
cd drugExplorer
source .venv/bin/activate
python application.py
```
**Access:** http://localhost:8002

---

## Demo Deployment

```bash
# Copy to demo folder
cp -r drugExplorer/build demo/
cp -r drugExplorer/data demo/
cp drugExplorer/*.py demo/
cp drugExplorer/requirements.txt demo/

# Run demo
cd demo
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
python application.py
```

---

## File Structure

```
txgnn/
├── txgnn_company_repurpose_end2end.py   # Step 1
├── process_all_drugs.py                  # Step 2
├── generate_all_deep_paths.py            # Step 3
├── drugExplorer/                         # Steps 4-5
│   ├── src/                              # React source
│   ├── build/                            # Built frontend
│   ├── data/                             # Data files
│   └── application.py                    # Flask server
└── demo/                                 # Portable demo
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 8002 in use | `pkill -f "python.*application.py"` |
| No drugs showing | Check `drugExplorer/data/your_predictions.csv` |
| Slow first load | Normal - data is cached |
| Paths missing | Run `generate_all_deep_paths.py` |
