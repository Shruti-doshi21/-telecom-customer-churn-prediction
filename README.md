# Telecom Customer Churn Prediction

## Project Overview

Customer churn is one of the biggest challenges faced by telecom companies. Acquiring a new customer is much more expensive than retaining an existing one.

The objective of this project is to build a Machine Learning model that predicts whether a customer is likely to churn based on customer demographics, account information, and subscribed services.

This project follows a complete end-to-end Machine Learning workflow, including data preprocessing, exploratory data analysis, model building, evaluation, feature importance analysis, business insights, and deployment using Streamlit.

#  Dataset

**Dataset:** Telco Customer Churn Dataset

The dataset contains customer information such as:

- Customer demographics
- Contract type
- Internet service
- Payment method
- Monthly charges
- Total charges
- Customer tenure
- Additional services
- Churn status

Target Variable:

**Churn**
- 0 → Customer will stay
- 1 → Customer will churn

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost
- Streamlit
- Joblib

# Project Workflow

### 1. Data Cleaning
- Removed Customer ID
- Checked missing values
- Converted TotalCharges into float
- Removed duplicate records

### 2. Data Preprocessing
- Label Encoding
- One-Hot Encoding
- Train-Test Split

### 3. Machine Learning Models

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

### 4. Model Evaluation

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score


# Final Model

After comparing all models, **Logistic Regression** was selected as the final model because it achieved the best overall balance across all evaluation metrics.


#  Business Insights

The most important factors affecting customer churn were:

- Customer Tenure
- Contract Type
- Internet Service
- Monthly Charges
- Total Charges
- Payment Method
- Online Security

Key Findings:

- Customers with longer tenure are less likely to churn.
- Customers with Two-Year Contracts have the lowest churn rate.
- Fiber Optic customers are more likely to churn.
- Customers paying through Electronic Check have higher churn probability.
- Higher Monthly Charges increase churn risk.
- Online Security improves customer retention.


# Business Recommendations

- Improve retention strategies for new customers.
- Encourage customers to switch to long-term contracts.
- Improve Fiber Optic customer experience.
- Promote Online Security services.
- Introduce loyalty discounts for high-risk customers.
- Encourage AutoPay payment methods.


#  Streamlit Application

The project includes an interactive Streamlit web application where users can:

- Enter customer information
- Predict customer churn
- View prediction results instantly


# Project Structure

Telecom-Customer-Churn/
│
├── app.py
├── telecom_customer_churn.ipynb
├── telecom_churn_model.pkl
├── feature_names.pkl
├── requirements.txt
├── README.md
└── Telco-Customer-Churn.csv


# How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit

```bash
streamlit run app.py
```

# Skills Demonstrated

- Data Cleaning
- Data Preprocessing
- Feature Engineering
- Exploratory Data Analysis
- Classification Models
- Model Evaluation
- Feature Importance Analysis
- Business Insights
- Streamlit Deployment

# Author

**Shruti Doshi**

Aspiring Data Scientist passionate about solving real-world business problems using Machine Learning and Data Analytics.
