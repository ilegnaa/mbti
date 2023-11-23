import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import pickle

# Load the trained model
loaded_model = pickle.load(('mbti_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Streamlit app
def main():
    st.title('MBTI Personality Prediction App')

    # User selects personality type
    selected_type = st.selectbox('Select your personality type:', ['INFJ', 'ENFP', 'INTP', 'ISTJ'])

    # User enters posts for prediction
    user_input = st.text_area('Enter your posts here:')

    # Make prediction when the user clicks the button
    if st.button('Predict'):
        if user_input:
            # Convert the user input to numerical format using the loaded vectorizer
            user_input_vec = vectorizer.transform([user_input])

            # Make predictions
            prediction = loaded_model.predict(user_input_vec)

            st.success(f'Predicted Personality Type: {prediction[0]}')
        else:
            st.warning('Please enter your posts for prediction.')

if _name_ == '_main_':
    main()
