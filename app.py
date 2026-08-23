
import streamlit as st
import numpy as np
import joblib
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title = "Student Exam Score Prediction", page_icon = "📊")

model = joblib.load("best_model.pkl")

st.title("Student Exam Score Prediction Based on Habits and Lifestyle Factors")
study_hours = st.number_input("Study Hours Per Day", min_value = 0.0, max_value = 12.0)
attendance = st.number_input("Attendance Percentage", min_value = 0.0, max_value = 100.0)
mental_health = st.number_input("Mental Health Rating", min_value = 0.0, max_value = 10.0)
sleep_hours = st.number_input("Sleep Hours", min_value = 0.0, max_value = 12.0)
social_media_hours = st.number_input("Social Media Hours", min_value = 0.0, max_value = 24.0)
part_time_job = st.selectbox("Part Time Job", ["Yes", "No"])
part_time_job_encoded = 1 if part_time_job == "Yes" else 0

if st.button("Predict Exam Score"):
    input_data = np.array([[study_hours, attendance, mental_health, sleep_hours, social_media_hours, part_time_job_encoded]])
    prediction = model.predict(input_data)
    prediction = max(0, min(100, prediction))
    st.success(f"Predicted Exam Score: {prediction:.2f}")
