
import pickle
import pandas as pd
import sys

def predict_reimbursement(days, miles, receipts):
    """Predict reimbursement using trained model"""
    # Load model
    with open('ml_model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    # Create features
    data = {
        'days': days,
        'miles': miles,
        'receipts': receipts,
        'days_sq': days ** 2,
        'miles_sq': miles ** 2,
        'receipts_sq': receipts ** 2,
        'miles_per_day': miles / days,
        'receipts_per_day': receipts / days,
        'miles_receipts': miles * receipts,
        'days_miles': days * miles,
        'days_receipts': days * receipts,
        'efficiency': miles / (days * receipts + 1e-6)
    }
    
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return round(prediction, 2)

if __name__ == "__main__":
    days = int(sys.argv[1])
    miles = float(sys.argv[2])
    receipts = float(sys.argv[3])
    print(predict_reimbursement(days, miles, receipts))
