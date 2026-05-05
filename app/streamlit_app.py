import streamlit as st
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.generator import generate_fake_news
from src.predict import predict_news

st.title("📰 Fake News Generator & Detector")

menu = st.sidebar.selectbox(
    "Select Feature",
    ["Generate Fake News", "Detect News"]
)

if menu == "Generate Fake News":
    topic = st.text_input("Enter Topic")

    if st.button("Generate"):
        if topic:
            news = generate_fake_news(topic)
            st.write(news)

elif menu == "Detect News":
    article = st.text_area("Paste News Article")

    if st.button("Detect"):
        if article:
            result = predict_news(article)
            st.subheader(result)
