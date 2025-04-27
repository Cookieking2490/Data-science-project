import streamlit as st
import joblib

model = joblib.load("sentiment_model.pkl")

st.title("Sentiment Classifier")
st.write("Enter a comment to predict sentiment (-1: Negative, 0: Neutral, 1: Positive)")

text = st.text_area("Your Comment:")

if st.button("Predict"):
    if text.strip() == "":
        st.warning("Please enter a comment.")
    else:
        prediction = model.predict([text])[0]
        label = { -1: "Negative", 0: "Neutral", 1: "Positive" }.get(prediction, "Unknown")
        st.success(f"Predicted Sentiment: **{label}**")

