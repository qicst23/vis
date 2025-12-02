# Amgen Drug Explorer - Demo Package

This is a standalone demo package for the TxGNN Drug Repurposing Visualization.

## Requirements

- Python 3.8 or higher
- Web browser (Chrome, Firefox, Edge, etc.)

## Quick Start (Windows 11)

### Step 1: Install Python Dependencies

Open Command Prompt or PowerShell and navigate to this folder:

```cmd
cd path\to\demo
pip install -r requirements.txt
```

### Step 2: Start the Server

```cmd
python application.py --host 0.0.0.0 --port 8002
```

### Step 3: Open Browser

Open your web browser and go to:

```
http://localhost:8002
```

## Features

This visualization includes:

1. **Meta-Path View** - Shows paths connecting drugs to predicted diseases
2. **Node Attention** - Multi-level attention tree for drug and disease nodes
3. **Sub-Graph** - Interactive force-directed network visualization
4. **Disease Embeddings** - Scatter plot of disease embeddings

## Available Drugs (28)

The following Amgen/Horizon drugs are available for exploration:

| # | Drug Name |
|---|-----------|
| 1 | adalimumab |
| 2 | apremilast |
| 3 | bevacizumab |
| 4 | blinatumomab |
| 5 | carfilzomib |
| 6 | cinacalcet |
| 7 | cysteamine |
| 8 | darbepoetin alfa |
| 9 | denosumab |
| 10 | erenumab |
| 11 | etanercept |
| 12 | etelcalcetide |
| 13 | evolocumab |
| 14 | filgrastim |
| 15 | glycerol phenylbutyrate |
| 16 | inebilizumab |
| 17 | infliximab |
| 18 | interferon gamma-1b |
| 19 | panitumumab |
| 20 | pegfilgrastim |
| 21 | pegloticase |
| 22 | rituximab |
| 23 | romiplostim |
| 24 | romosozumab |
| 25 | talimogene laherparepvec |
| 26 | teprotumumab |
| 27 | tezepelumab |
| 28 | trastuzumab |

## Usage Instructions

1. **Select a Drug**: Use the dropdown in the left sidebar to select a drug
2. **View Disease Candidates**: The sidebar shows predicted disease candidates with scores
3. **Select Diseases**: Click on diseases in the candidate list to explore their paths
4. **Switch Views**: Use the tabs to switch between Meta-Path, Node Attention, Sub-Graph, and Disease Embeddings

## Troubleshooting

### Port already in use
If port 8002 is already in use, change the port number:
```cmd
python application.py --host 0.0.0.0 --port 8080
```

### Module not found
Make sure you've installed the requirements:
```cmd
pip install -r requirements.txt
```

### Blank page
Wait a few seconds for the page to load, or refresh the browser.

## File Structure

```
demo/
├── application.py      # Flask application entry point
├── api.py              # API endpoints
├── database_json.py    # Data loading and queries
├── vis.py              # Static file serving
├── utils.py            # Utility functions
├── requirements.txt    # Python dependencies
├── README.md           # This file
├── build/              # Frontend build files
│   ├── index.html
│   └── static/
├── data/               # Visualization data
│   ├── your_predictions.csv
│   ├── attention_all.csv
│   ├── precomputed_paths.json
│   ├── subgraphs.json
│   └── ...
└── txgnn_data/         # Node and edge type definitions
    ├── node_types.json
    └── edge_types.json
```

## Contact

For questions or issues, please contact the development team.

# vis
