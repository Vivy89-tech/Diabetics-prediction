
import streamlit as st
import numpy as np
import pandas as pd
model = joblib.load("/content/diabetes_model.joblib")

#create a title for the app
st.title("Diabetics Prediction App")
col1,col2 = st.columns(2)
st.write("Enter the following details to predict diabetics:")

#Creating input fields for each features

Pregnancies= col1.number_input(label="Number of pregnancies", min_value=0, max_value=17)
Glucose = col2.number_input(label= "Enter Glucose level", min_value=0, max_value=191)
BloodPressure = col1.number_input(label="Enter Blood pressure level", min_value=0,max_value=114)
SkinThickness=col2.number_input(label="Enter Skin thickness level", min_value=0,max_value=99)
Insulin=col1.number_input(label="Enter insulin level", min_value=0,max_value=846)
BMI=col2.number_input(label="Enter BMI Score", min_value=0,max_value=67)
DiabetesPredigreeFunction=col1.number_input(label="Enter DBF Score",min_value=0.078,max_value=2.42)
Age=col2.number_input(label="Enter Age",min_value=21,max_value=81)

#Predict button
if st.button("Predict"):
#prepare input for prediction
    input_data = [[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPredigreeFunction,Age]]

#make prediction

    prediction=model.predict(input_data)
#Result
    if prediction [0] == 1:
        st.write ("prediction:Positive for Diabetics")
    else:
        st.write("prediction:Negative for Diabetics")


