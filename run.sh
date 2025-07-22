#!/bin/bash

# Top Coder Challenge - Reimbursement System Prediction
# Usage: ./run.sh <trip_duration_days> <miles_traveled> <total_receipts_amount>

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Activate virtual environment if available, otherwise use system python
if [ -d "$SCRIPT_DIR/ml_env" ]; then
    source "$SCRIPT_DIR/ml_env/bin/activate"
fi

# Use python3 to run the prediction
python3 "$SCRIPT_DIR/predict.py" "$@"
