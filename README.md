# 🔮 Customer Churn Prediction using Decision Tree
![Decision Tree](tree_visualization(2).png)

## 📊 Project Overview
Built a **Decision Tree classifier** to predict which customers will churn (cancel service). 
- **Accuracy:** 80%
- **AUC-ROC:** 0.82
- **Interpretable rules** that business teams can action

## 🎯 Business Impact
- Identifies high-risk customers with **68% churn rate**
- Potential annual savings: **$1.4M+**
- Provides **explainable predictions** (not a black box)

## 📁 Repository Structure
├── churn_prediction_project.ipynb # Complete analysis & modeling
├── predict_churn.py # Prediction function
├── decision_tree_churn_model.pkl # Trained model
├── label_encoders.pkl # For text-to-number conversion
└── feature_names.csv # Column names used by model

text

## 🔍 Key Findings
| Feature | Impact |
|---------|--------|
| **Contract type** | Month-to-month = 68% churn rate |
| **Tenure** | <12 months = high risk |
| **Monthly charges** | >$70 = 45% churn rate |

### Sample Business Rule:
IF Contract = 'Month-to-month' AND tenure < 12 months
THEN Churn Probability = 75% → Offer retention discount

text

## 🚀 How to Use

**Prerequisites:** Make sure all files are in the same folder:
- `predict_churn.py`
- `decision_tree_churn_model.pkl`
- `label_encoders.pkl`
- `feature_names.csv`

```python
from predict_churn import predict_churn

customer = {
    'gender': 'Male',
    'tenure': 3,
    'MonthlyCharges': 85.5,
    'Contract': 'Month-to-month'
}

result = predict_churn(customer)
print(f"Will churn? {result['Churn']} ({result['Probability']})")
📈 Model Performance
Metric	Score
Accuracy	80%
Precision (Churn)	0.65
Recall (Churn)	0.58
AUC-ROC	0.82
🛠 Technologies
Python 3.9+

pandas, scikit-learn, matplotlib

Decision Tree Classifier

Google Colab / Jupyter

👨‍💻 Author
**Sunday Oliseh Otieno**
LinkedIn :www.linkedin.com/in/oliseh-sunday-2a0468268
Github:https://github.com/DA-Oliseh

📅 Project Date
May 2026
