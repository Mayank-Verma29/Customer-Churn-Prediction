
import streamlit as st
import pickle
import pandas as pd
import numpy as np
model = pickle.load(open("lr_model.pkl","rb"))
st.title("Customer Churn Prediction App")
st.write("Enter customer details below : ")
Tenure = st.slider("Tenure (Months) ",0,72)
MonthlyCharges = st.number_input("Monthly Charges")
AvgMonthlySpend = st.number_input("AvgMonthlySpend")
TotalCharges = st.number_input("Total Charges")
Age = st.number_input("Age")
Gender = st.selectbox("Gender",["Male","Female"])
Contract = st.selectbox("Contract Type",["Month-to-month","One year","Two year"])
PaymentMethod = st.selectbox("Payment methods",["Bank transfer","Mailed check","Electronic check","Credit card"])
Tenure_Group = st.selectbox("Tenure Group",["Long-term","Mid-term","New"])
Is_a_Long_Contract = st.selectbox("Long Contract",["Yes","No"])
High_Charges = st.selectbox("High Charges",["Yes","No"])

Age = float(Age)
Tenure = float(Tenure)
MonthlyCharges = float(MonthlyCharges)
TotalCharges = float(TotalCharges)
AvgMonthlySpend = float(AvgMonthlySpend)
Is_a_Long_Contract = 1 if Is_a_Long_Contract == "Yes" else 0
High_Charges = 1 if High_Charges == "Yes" else 0

if st.button("Predict"):
    features = pd.DataFrame(
    [[
        Age,
        Tenure,
        MonthlyCharges,
        TotalCharges,
        AvgMonthlySpend,
        Is_a_Long_Contract,
        High_Charges,
        Gender,
        Contract,
        PaymentMethod,
        Tenure_Group
    ]],

    columns = [
        "Age","Tenure","MonthlyCharges","TotalCharges","AvgMonthlySpend",
        "Is_a_Long_Contract","High_Charges",
        "Gender","Contract","PaymentMethod","Tenure_Group"
    ]
)
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.error("Customer is likely to Churn")
    else:
        st.success("Customer is likely to Stay")

