# Top Coder Challenge: Legacy Reimbursement System

## Solution Approach

This solution reverse-engineers a 60-year-old legacy reimbursement system using machine learning techniques. The approach achieved a score of **2899**, significantly beating the target of 6263.

### Key Components:

1. **Feature Engineering**: Created optimized features including:
   - Basic inputs: trip duration, miles traveled, receipt amounts
   - Polynomial features: squares of inputs
   - Ratio features: miles per day, receipts per day
   - Interaction features: cross-products of inputs
   - Efficiency metrics: miles/(days × receipts)

2. **Machine Learning Model**: 
   - Gradient Boosting Regressor optimized for Mean Absolute Error
   - 200 estimators with depth 4 for robust generalization
   - Huber loss for robustness to outliers
   - Cross-validated performance: ~$28 average error

3. **Performance**:
   - **Exact matches**: 0 (±$0.01)
   - **Close matches**: 25/1000 (±$1.00) = 2.5%
   - **Average error**: $27.99
   - **Final Score**: 2899 ✅

## Files

- `run.sh`: Main prediction script (executable Python)
- `ml_model.pkl`: Trained machine learning model
- `private_results.txt`: Results for 5000 private test cases
- `LICENSE`: MIT License

## Usage

```bash
./run.sh <trip_duration_days> <miles_traveled> <total_receipts_amount>
```

Example:
```bash
./run.sh 5 250 150.75
# Output: 634.59
```

## Dependencies

- Python 3.x
- pandas>=1.3.0
- scikit-learn>=1.0.0  
- numpy>=1.20.0

Install dependencies:
```bash
pip install -r requirements.txt
```

The solution is designed to work with standard Python scientific libraries and should run efficiently on any modern system.
