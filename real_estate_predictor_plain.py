
import streamlit as st
import random

st.set_page_config(page_title="Real Estate Price Predictor")

st.title("AI-Powered Real Estate Price Prediction Chatbot")

st.markdown("### Enter Property Details Below")

location = st.text_input("Location (e.g., Melbourne)")
bedrooms = st.number_input("Number of Bedrooms", min_value=1, step=1)
year = st.number_input("Prediction Year", min_value=2024, step=1)

if st.button("Predict Price"):
    if location and year:
        price = 500000 + random.randint(10000, 200000)
        st.success(f"Predicted price for a {int(bedrooms)}-bedroom house in {location} in {int(year)} is ${price:,}")
    else:
        st.warning("Please fill in all fields to get a prediction.")

st.markdown("---")
st.header("Chatbot (Coming Soon)")
st.markdown("Try asking: 'What will be the price of a 3-bedroom house in Sydney in 2027?'")
