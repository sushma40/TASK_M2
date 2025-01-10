import streamlit as st
import pickle
import numpy as np

# Load the model using pickle
with open('linear_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Sales Prediction App")

# Get user input using Streamlit widgets
tv = st.number_input("Enter TV advertising budget:", min_value=0.0, step=0.1)
radio = st.number_input("Enter Radio advertising budget:", min_value=0.0, step=0.1)
newspaper = st.number_input("Enter Newspaper advertising budget:", min_value=0.0, step=0.1)

# Button to trigger prediction
if st.button('Predict'):
    
        # Prepare the input data as an array
    input_data = np.array([[tv, radio, newspaper]])

        # Make the prediction
    predicted_sales = model.predict(input_data)

        # Show the predicted sales
    st.write(f"Predicted Sales: {predicted_sales[0]}")
