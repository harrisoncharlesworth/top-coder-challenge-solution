#!/bin/bash

# Top Coder Challenge - Reimbursement System Prediction
# Usage: ./run.sh <trip_duration_days> <miles_traveled> <total_receipts_amount>

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Use python3 to run the prediction
python3 "$SCRIPT_DIR/predict.py" "$@"
