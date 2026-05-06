import streamlit as st
import sys
import os
import time

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import your backend functions
from src.generator import generate_fake_news
from src.predict import predict_news

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(
    page_title="Veritas | AI News Studio",
    page_icon="📰",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for a cleaner header
st.markdown("""
    <style>
    .main-title { text-align: center; font-size: 3rem; font-weight: 700; margin-bottom: 0; }
    .sub-title { text-align: center; color: #666; margin-top: 0; margin-bottom: 2rem; }
    </style>
""", unsafe_allow_html=True)

# Main Header
st.markdown('<p class="main-title">📰 Veritas Studio</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">AI-Powered News Generation & Detection</p>', unsafe_allow_html=True)

# 2. Upgraded Sidebar
with st.sidebar:
    st.title("Navigation")
    menu = st.radio(
        "Choose a tool:",
        ["✍️ Generate News", "🔍 Detect News"],
        help="Select whether you want to generate a synthetic article or verify an existing one."
    )
    
    st.divider()
    st.markdown("### About")
    st.info("This tool uses NLP models to demonstrate synthetic text generation and detect potentially misleading news articles.")

# -----------------------------------------
# FEATURE 1: GENERATE NEWS
# -----------------------------------------
if menu == "✍️ Generate News":
    st.header("Synthetic News Generator")
    st.write("Enter a topic below, and the AI will draft a synthetic news article based on your prompt.")
    
    # Using a form prevents accidental re-runs if the user presses 'Enter' too early
    with st.form("generate_form"):
        topic = st.text_input("What should the article be about?", placeholder="e.g., The Discovery of a New Planet...")
        
        # Adding some fake UI elements for future expansion (Optional)
        col1, col2 = st.columns(2)
        with col1:
            tone = st.selectbox("Tone (Placeholder)", ["Objective", "Sensational", "Satirical"])
        with col2:
            length = st.select_slider("Length (Placeholder)", options=["Short", "Medium", "Long"])
            
        submitted = st.form_submit_button("Generate Article 🚀", use_container_width=True)

    if submitted:
        if topic.strip():
            # Give the user visual feedback that the model is working
            with st.spinner("🧠 AI is drafting your article. Please wait..."):
                news = generate_fake_news(topic) 
                
            st.success("Article generated successfully!")
            
            # Displaying the text in a stylized container
            st.markdown("### Generated Draft")
            st.info(news, icon="🗞️")
            
            # Let the user download the result
            st.download_button(
                label="⬇️ Download as TXT",
                data=news,
                file_name=f"{topic.replace(' ', '_')}_article.txt",
                mime="text/plain"
            )
        else:
            st.warning("⚠️ Please enter a topic before generating.")

# -----------------------------------------
# FEATURE 2: DETECT NEWS
# -----------------------------------------
elif menu == "🔍 Detect News":
    st.header("News Authenticity Detector")
    st.write("Paste the text of a news article below to analyze its likelihood of being synthetic or fake.")
    
    article = st.text_area("Article Content", height=250, placeholder="Paste the full text of the article here...")
    
    # Center the button using columns
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        detect_btn = st.button("Analyze Article 🔎", use_container_width=True)

    if detect_btn:
        if article.strip():
            with st.spinner("🕵️‍♂️ Analyzing linguistic patterns and cross-referencing..."):
                result = predict_news(article)
                
            st.markdown("### Analysis Result")
            
            # Make the output visual based on the result
            # (Assuming your predict_news returns strings like "Fake" or "Real")
            if "fake" in str(result).lower() or "false" in str(result).lower():
                st.error(f"**Prediction:** {result} 🚨")
            elif "real" in str(result).lower() or "true" in str(result).lower():
                st.success(f"**Prediction:** {result} ✅")
            else:
                st.info(f"**Prediction:** {result}")
                
            # Use an expander to keep the UI clean if you want to add more stats later
            with st.expander("View Detailed Metrics"):
                st.write(f"**Character Count:** {len(article)}")
                st.write(f"**Word Count:** {len(article.split())}")
                st.caption("Future updates will display sentiment analysis and sentence complexity here.")
        else:
            st.warning("⚠️ Please paste an article to analyze.")
