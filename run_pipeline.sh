#!/bin/bash
#===============================================================================
# TxGNN Drug Repurposing Pipeline
# 
# This script runs the complete pipeline for all Amgen and Horizon drugs:
#   Step 1: TxGNN Predictions
#   Step 2: Data Processing for Visualization
#   Step 3: Deep Path Generation (2-5 hops)
#   Step 4: Build Frontend
#   Step 5: (Optional) Start Server
#
# Usage:
#   ./run_pipeline.sh                    # Run all steps
#   ./run_pipeline.sh --skip-predictions # Skip Step 1 (use existing predictions)
#   ./run_pipeline.sh --start-server     # Start server after pipeline
#   ./run_pipeline.sh --help             # Show help
#
# Author: TxGNN Team
# Date: December 2025
#===============================================================================

set -e  # Exit on error

#-------------------------------------------------------------------------------
# Configuration
#-------------------------------------------------------------------------------
PROJECT_ROOT="/home/nchen10/cursor_prjs/txgnn"
DATA_DIR="${PROJECT_ROOT}/data"
MODEL_DIR="${PROJECT_ROOT}/model_ckpt"
OUTPUT_DIR="${PROJECT_ROOT}/repurpose_out"
DRUGEXPLORER_DIR="${PROJECT_ROOT}/drugExplorer"
DEVICE="cuda:0"  # Change to "cpu" if no GPU available
TOP_DISEASES=100  # Number of disease candidates per drug

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

#-------------------------------------------------------------------------------
# Parse Arguments
#-------------------------------------------------------------------------------
SKIP_PREDICTIONS=false
START_SERVER=false
SINGLE_DRUG=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --skip-predictions)
            SKIP_PREDICTIONS=true
            shift
            ;;
        --start-server)
            START_SERVER=true
            shift
            ;;
        --device)
            DEVICE="$2"
            shift 2
            ;;
        --top-diseases)
            TOP_DISEASES="$2"
            shift 2
            ;;
        --drug)
            SINGLE_DRUG="$2"
            shift 2
            ;;
        --help|-h)
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --skip-predictions    Skip Step 1 (use existing predictions)"
            echo "  --start-server        Start server after pipeline completes"
            echo "  --device DEVICE       Compute device (default: cuda:0)"
            echo "  --top-diseases N      Number of disease candidates (default: 100)"
            echo "  --drug NAME           Process single drug only"
            echo "  --help                Show this help message"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

#-------------------------------------------------------------------------------
# Helper Functions
#-------------------------------------------------------------------------------
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo ""
    echo -e "${BLUE}================================================================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}================================================================================${NC}"
    echo ""
}

check_file_exists() {
    if [ ! -f "$1" ]; then
        log_error "Required file not found: $1"
        exit 1
    fi
}

check_dir_exists() {
    if [ ! -d "$1" ]; then
        log_error "Required directory not found: $1"
        exit 1
    fi
}

get_elapsed_time() {
    local start=$1
    local end=$(date +%s)
    local elapsed=$((end - start))
    local minutes=$((elapsed / 60))
    local seconds=$((elapsed % 60))
    echo "${minutes}m ${seconds}s"
}

#-------------------------------------------------------------------------------
# Main Pipeline
#-------------------------------------------------------------------------------
main() {
    print_header "TxGNN DRUG REPURPOSING PIPELINE"
    
    PIPELINE_START=$(date +%s)
    
    log_info "Project Root: ${PROJECT_ROOT}"
    log_info "Device: ${DEVICE}"
    log_info "Top Diseases: ${TOP_DISEASES}"
    if [ -n "$SINGLE_DRUG" ]; then
        log_info "Single Drug Mode: ${SINGLE_DRUG}"
    fi
    echo ""

    # Navigate to project root
    cd "${PROJECT_ROOT}"

    # Activate virtual environment
    if [ -f ".venv/bin/activate" ]; then
        source .venv/bin/activate
        log_success "Activated virtual environment"
    else
        log_warning "Virtual environment not found, using system Python"
    fi

    #---------------------------------------------------------------------------
    # Step 1: TxGNN Predictions
    #---------------------------------------------------------------------------
    if [ "$SKIP_PREDICTIONS" = false ]; then
        print_header "STEP 1: Running TxGNN Predictions"
        STEP1_START=$(date +%s)

        check_file_exists "${PROJECT_ROOT}/txgnn_company_repurpose_end2end.py"
        check_dir_exists "${DATA_DIR}"
        check_dir_exists "${MODEL_DIR}"

        if [ -n "$SINGLE_DRUG" ]; then
            # Single drug mode
            echo "${SINGLE_DRUG}" > /tmp/single_drug.txt
            log_info "Processing single drug: ${SINGLE_DRUG}"
            
            python txgnn_company_repurpose_end2end.py \
                --data_dir "${DATA_DIR}" \
                --ckpt_dir "${MODEL_DIR}" \
                --out_dir "${OUTPUT_DIR}" \
                --device "${DEVICE}" \
                --company custom \
                --custom_drug_list /tmp/single_drug.txt \
                --relation indication \
                --fuzzy_match
        else
            # All Amgen + Horizon drugs
            log_info "Processing all Amgen and Horizon drugs"
            
            python txgnn_company_repurpose_end2end.py \
                --data_dir "${DATA_DIR}" \
                --ckpt_dir "${MODEL_DIR}" \
                --out_dir "${OUTPUT_DIR}" \
                --device "${DEVICE}" \
                --company both \
                --relation indication \
                --fuzzy_match
        fi

        log_success "Step 1 completed in $(get_elapsed_time $STEP1_START)"
    else
        log_warning "Skipping Step 1 (using existing predictions)"
    fi

    #---------------------------------------------------------------------------
    # Step 2: Process Data for Visualization
    #---------------------------------------------------------------------------
    print_header "STEP 2: Processing Data for Visualization"
    STEP2_START=$(date +%s)

    check_file_exists "${PROJECT_ROOT}/process_all_drugs.py"

    # Create output directory
    mkdir -p "${DRUGEXPLORER_DIR}/data"

    # Copy prediction data to visualization folder
    log_info "Copying prediction data..."
    cp -f "${DATA_DIR}/your_predictions.csv" "${DRUGEXPLORER_DIR}/data/" 2>/dev/null || true
    cp -f "${DATA_DIR}/attention_all.csv" "${DRUGEXPLORER_DIR}/data/" 2>/dev/null || true
    cp -f "${DATA_DIR}/disease_info.json" "${DRUGEXPLORER_DIR}/data/" 2>/dev/null || true
    cp -f "${DATA_DIR}/drug_info.json" "${DRUGEXPLORER_DIR}/data/" 2>/dev/null || true
    cp -f "${DATA_DIR}/drug_disease_score.json" "${DRUGEXPLORER_DIR}/data/" 2>/dev/null || true
    cp -f "${DATA_DIR}/disease_node_ids.json" "${DRUGEXPLORER_DIR}/data/" 2>/dev/null || true
    cp -f "${DATA_DIR}/attention_node_name_dict.json" "${DRUGEXPLORER_DIR}/data/" 2>/dev/null || true
    cp -f "${DATA_DIR}/meta_path_json.json" "${DRUGEXPLORER_DIR}/data/" 2>/dev/null || true

    # Run process_all_drugs.py
    if [ -n "$SINGLE_DRUG" ]; then
        log_info "Processing visualization data for: ${SINGLE_DRUG}"
        python process_all_drugs.py \
            --data_dir "${DATA_DIR}" \
            --predictions_dir "${OUTPUT_DIR}" \
            --output_dir "${DRUGEXPLORER_DIR}/data" \
            --ckpt_dir "${MODEL_DIR}" \
            --drug "${SINGLE_DRUG}" \
            --top_diseases "${TOP_DISEASES}"
    else
        log_info "Processing visualization data for all drugs"
        python process_all_drugs.py \
            --data_dir "${DATA_DIR}" \
            --predictions_dir "${OUTPUT_DIR}" \
            --output_dir "${DRUGEXPLORER_DIR}/data" \
            --ckpt_dir "${MODEL_DIR}" \
            --top_diseases "${TOP_DISEASES}"
    fi

    log_success "Step 2 completed in $(get_elapsed_time $STEP2_START)"

    #---------------------------------------------------------------------------
    # Step 3: Generate Deep Paths (2-5 hops)
    #---------------------------------------------------------------------------
    print_header "STEP 3: Generating Deep Paths (2-5 hops)"
    STEP3_START=$(date +%s)

    check_file_exists "${PROJECT_ROOT}/generate_all_deep_paths.py"

    log_info "Generating deep paths for drug-disease pairs..."
    
    python generate_all_deep_paths.py

    log_success "Step 3 completed in $(get_elapsed_time $STEP3_START)"

    #---------------------------------------------------------------------------
    # Step 4: Build Frontend
    #---------------------------------------------------------------------------
    print_header "STEP 4: Building Frontend"
    STEP4_START=$(date +%s)

    cd "${DRUGEXPLORER_DIR}"

    # Check if npm is available
    if ! command -v npm &> /dev/null; then
        log_error "npm not found. Please install Node.js and npm."
        exit 1
    fi

    # Install dependencies if needed
    if [ ! -d "node_modules" ]; then
        log_info "Installing npm dependencies..."
        npm install
    fi

    # Build production bundle
    log_info "Building production bundle..."
    npm run build

    log_success "Step 4 completed in $(get_elapsed_time $STEP4_START)"

    #---------------------------------------------------------------------------
    # Step 5: Generate Path Explanation Documents
    #---------------------------------------------------------------------------
    print_header "STEP 5: Generating Path Explanation Documents"
    STEP5_START=$(date +%s)

    cd "${PROJECT_ROOT}"

    check_file_exists "${PROJECT_ROOT}/generate_path_explanations.py"

    log_info "Generating explanation markdown files for all drugs..."
    
    python generate_path_explanations.py \
        --data_dir "${DRUGEXPLORER_DIR}/data" \
        --output_dir "${DRUGEXPLORER_DIR}/docs"

    log_success "Step 5 completed in $(get_elapsed_time $STEP5_START)"

    #---------------------------------------------------------------------------
    # Step 6: Update Demo Folder
    #---------------------------------------------------------------------------
    print_header "STEP 6: Updating Demo Folder"
    STEP6_START=$(date +%s)

    cd "${PROJECT_ROOT}"

    # Create demo folder
    mkdir -p demo

    # Copy backend files
    log_info "Copying backend files..."
    cp -f "${DRUGEXPLORER_DIR}/api.py" demo/
    cp -f "${DRUGEXPLORER_DIR}/database_json.py" demo/
    cp -f "${DRUGEXPLORER_DIR}/application.py" demo/
    cp -f "${DRUGEXPLORER_DIR}/utils.py" demo/
    cp -f "${DRUGEXPLORER_DIR}/requirements.txt" demo/

    # Copy frontend build
    log_info "Copying frontend build..."
    rm -rf demo/build
    cp -r "${DRUGEXPLORER_DIR}/build" demo/

    # Copy data
    log_info "Copying data files..."
    rm -rf demo/data
    cp -r "${DRUGEXPLORER_DIR}/data" demo/

    # Copy documentation
    log_info "Copying documentation..."
    cp -f docs/*.md demo/ 2>/dev/null || true
    cp -f "${DRUGEXPLORER_DIR}/docs/"*.md demo/ 2>/dev/null || true

    log_success "Step 6 completed in $(get_elapsed_time $STEP6_START)"

    #---------------------------------------------------------------------------
    # Summary
    #---------------------------------------------------------------------------
    print_header "PIPELINE COMPLETE"
    
    TOTAL_TIME=$(get_elapsed_time $PIPELINE_START)
    
    echo "Total execution time: ${TOTAL_TIME}"
    echo ""
    echo "Output locations:"
    echo "  Predictions:    ${OUTPUT_DIR}/per_drug/"
    echo "  Visualization:  ${DRUGEXPLORER_DIR}/data/"
    echo "  Demo package:   ${PROJECT_ROOT}/demo/"
    echo ""
    
    # Count files
    DRUG_COUNT=$(ls -1 "${OUTPUT_DIR}/per_drug/"*_repurposing.csv 2>/dev/null | wc -l)
    PATH_COUNT=$(ls -1 "${DRUGEXPLORER_DIR}/data/"*_scored_paths.json 2>/dev/null | wc -l)
    
    echo "Summary:"
    echo "  Drugs processed:     ${DRUG_COUNT}"
    echo "  Path files created:  ${PATH_COUNT}"
    echo ""

    #---------------------------------------------------------------------------
    # Optional: Start Server
    #---------------------------------------------------------------------------
    if [ "$START_SERVER" = true ]; then
        print_header "STARTING SERVER"
        
        cd "${DRUGEXPLORER_DIR}"
        
        # Check if port is in use
        if lsof -ti:8002 > /dev/null 2>&1; then
            log_warning "Port 8002 is in use, killing existing process..."
            lsof -ti:8002 | xargs kill -9
            sleep 2
        fi
        
        # Activate drugExplorer venv if exists
        if [ -f ".venv/bin/activate" ]; then
            source .venv/bin/activate
        fi
        
        log_info "Starting Flask server on http://localhost:8002"
        python application.py
    else
        echo ""
        echo "To start the visualization server:"
        echo "  cd ${DRUGEXPLORER_DIR}"
        echo "  source .venv/bin/activate"
        echo "  python application.py"
        echo ""
        echo "Then open: http://localhost:8002"
    fi
}

#-------------------------------------------------------------------------------
# Run Main
#-------------------------------------------------------------------------------
main "$@"
