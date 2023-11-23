import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('mbti_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# Function to make predictions
def predict_personality(input_data):
    # Preprocess input_data if needed (should match the preprocessing used during training)
    # For simplicity, assume input_data is a DataFrame with the same structure as the training data
    predictions = loaded_model.predict(input_data)
    return predictions

# Streamlit app
def main():
    st.title('MBTI Personality Prediction App')

    # Input features for prediction
    st.sidebar.header('User Input Features')
    
    # Example: Assuming four features for simplicity, adjust as per your dataset
    feature1 = st.sidebar.slider('Feature 1', min_value=0, max_value=10, value=5)
    feature2 = st.sidebar.slider('Feature 2', min_value=0, max_value=10, value=5)
    feature3 = st.sidebar.slider('Feature 3', min_value=0, max_value=10, value=5)
    feature4 = st.sidebar.slider('Feature 4', min_value=0, max_value=10, value=5)

    # Create a DataFrame from user input
    user_input = pd.DataFrame({'Feature1': [feature1], 'Feature2': [feature2],
                               'Feature3': [feature3], 'Feature4': [feature4]})

    # Make predictions
    if st.button('Predict'):
        predictions = predict_personality(user_input)
        st.success(f'Predicted Personality Type: {predictions[0]}')

if _name_ == '_main_':
    main()
