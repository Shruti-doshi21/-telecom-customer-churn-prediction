import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("telecom_churn_model.pkl")

st.set_page_config(page_title="Telecom Customer Churn Prediction")

st.title(" Telecom Customer Churn Prediction")
st.write("Predict whether a customer is likely to churn.")

# User Inputs

gender = st.selectbox("Gender", ["Female","Male"])

SeniorCitizen = st.selectbox("Senior Citizen", ["No","Yes"])

Partner = st.selectbox("Partner",["No","Yes"])

Dependents = st.selectbox("Dependents",["No","Yes"])

tenure = st.slider("Tenure (Months)",0,72,12)

PhoneService = st.selectbox("Phone Service",["No","Yes"])

PaperlessBilling = st.selectbox("Paperless Billing",["No","Yes"])

MonthlyCharges = st.number_input("Monthly Charges",0.0,150.0,70.0)

TotalCharges = st.number_input("Total Charges",0.0,10000.0,1000.0)

InternetService = st.selectbox(
    "Internet Service",
    ["DSL","Fiber optic","No"]
)

Contract = st.selectbox(
    "Contract",
    ["Month-to-month","One year","Two year"]
)

PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check"
    ]
)

# Encode Inputs

gender = 1 if gender=="Male" else 0
SeniorCitizen = 1 if SeniorCitizen=="Yes" else 0
Partner = 1 if Partner=="Yes" else 0
Dependents = 1 if Dependents=="Yes" else 0
PhoneService = 1 if PhoneService=="Yes" else 0
PaperlessBilling = 1 if PaperlessBilling=="Yes" else 0

data = {
"gender":[gender],
"SeniorCitizen":[SeniorCitizen],
"Partner":[Partner],
"Dependents":[Dependents],
"tenure":[tenure],
"PhoneService":[PhoneService],
"PaperlessBilling":[PaperlessBilling],
"MonthlyCharges":[MonthlyCharges],
"TotalCharges":[TotalCharges]
}

df = pd.DataFrame(data)

# Dummy columns

df["MultipleLines_No phone service"]=0
df["MultipleLines_Yes"]=0

df["InternetService_Fiber optic"]=1 if InternetService=="Fiber optic" else 0
df["InternetService_No"]=1 if InternetService=="No" else 0

df["OnlineSecurity_No internet service"]=0
df["OnlineSecurity_Yes"]=0

df["OnlineBackup_No internet service"]=0
df["OnlineBackup_Yes"]=0

df["DeviceProtection_No internet service"]=0
df["DeviceProtection_Yes"]=0

df["TechSupport_No internet service"]=0
df["TechSupport_Yes"]=0

df["StreamingTV_No internet service"]=0
df["StreamingTV_Yes"]=0

df["StreamingMovies_No internet service"]=0
df["StreamingMovies_Yes"]=0

df["Contract_One year"]=1 if Contract=="One year" else 0
df["Contract_Two year"]=1 if Contract=="Two year" else 0

df["PaymentMethod_Credit card (automatic)"]=1 if PaymentMethod=="Credit card (automatic)" else 0
df["PaymentMethod_Electronic check"]=1 if PaymentMethod=="Electronic check" else 0
df["PaymentMethod_Mailed check"]=1 if PaymentMethod=="Mailed check" else 0

# Prediction

if st.button("Predict"):

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    if prediction==1:
        st.error(f"⚠ Customer is likely to Churn.\n\nProbability : {probability:.2%}")
    else:
        st.success(f"✅ Customer is likely to Stay.\n\nProbability of Churn : {probability:.2%}")