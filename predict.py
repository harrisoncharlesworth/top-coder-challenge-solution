#!/usr/bin/env python3

import pickle
import sys
import os

def predict_reimbursement(days, miles, receipts):
    """Predict reimbursement using trained model"""
    # Get script directory for relative paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, 'ml_model.pkl')
    
    # Load model
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    # Create features manually (avoiding pandas dependency)
    import numpy as np
    
    # Calculate features
    days_sq = days ** 2
    miles_sq = miles ** 2
    receipts_sq = receipts ** 2
    miles_per_day = miles / days
    receipts_per_day = receipts / days
    miles_receipts = miles * receipts
    days_miles = days * miles
    days_receipts = days * receipts
    efficiency = miles / (days * receipts + 1e-6)
    
    # Create feature array in the same order as training
    features = [
        days, miles, receipts, days_sq, miles_sq, receipts_sq,
        miles_per_day, receipts_per_day, miles_receipts, 
        days_miles, days_receipts, efficiency
    ]
    
    X = np.array(features).reshape(1, -1)
    prediction = model.predict(X)[0]
    return round(prediction, 2)

if __name__ == "__main__":
    days = int(sys.argv[1])
    miles = float(sys.argv[2])
    receipts = float(sys.argv[3])
    print(predict_reimbursement(days, miles, receipts))
