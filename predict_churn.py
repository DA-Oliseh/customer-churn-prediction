
import pandas as pd
import joblib

def predict_churn(customer_data):
    model = joblib.load('decision_tree_churn_model.pkl')
    encoders = joblib.load('label_encoders.pkl')
    feature_names = pd.read_csv('feature_names.csv').squeeze().tolist()
    
    df = pd.DataFrame([customer_data])
    
    for col in encoders:
        if col in df.columns:
            df[col] = encoders[col].transform(df[col])
    
    for col in feature_names:
        if col not in df.columns:
            df[col] = 0
    
    df = df[feature_names]
    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]
    
    return {'Churn': 'Yes' if pred == 1 else 'No', 'Probability': f"{prob*100:.1f}%"}

if __name__ == "__main__":
    sample = {'gender': 'Male', 'tenure': 12, 'MonthlyCharges': 85.5, 'Contract': 'Month-to-month'}
    print(predict_churn(sample))
