import streamlit as st
import requests

# Title of the Streamlit App
st.title("Heart Disease Prediction")

# Create the input form
st.subheader("Enter the following details:")

# Get the 6 input features from the user
age = st.number_input("Age", min_value=0, max_value=120, step=1)
resting_bp = st.number_input("Resting BP", min_value=0, max_value=200, step=1)
cholesterol = st.number_input("Cholesterol", min_value=0, max_value=600, step=1)
fasting_bs = st.selectbox("Fasting Blood Sugar (FBS)", options=[0, 1])  # 0 or 1 (yes or no)
max_hr = st.number_input("Max HR", min_value=0, max_value=220, step=1)
oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, step=0.1)

# Collect input features into a list
feature_vector = [age, resting_bp, cholesterol, fasting_bs, max_hr, oldpeak]

# Button to make the prediction
if st.button("Predict"):
    # Define the API endpoint
    url = "https://my-app-582321675359.us-central1.run.app/predict"
    
    # Prepare the data in the format expected by the API
    payload = {"feature_vector": feature_vector}

    # Send POST request to the FastAPI prediction endpoint
    response = requests.post(url, json=payload)

    # Display the result
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        if prediction[0] == 0:
            st.success("Prediction: No Heart Disease")
        else:
            st.error("Prediction: Heart Disease Detected")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")