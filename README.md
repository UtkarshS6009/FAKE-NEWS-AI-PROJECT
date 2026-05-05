📰 Fake News Generator & Detector
Generative AI + NLP Based News Classification System

🚀 Project Overview

This project is an AI-powered web application that can:

Generate realistic fake news articles using a Large Language Model (LLM).

Detect whether a news article is Fake or Real using Natural Language Processing (NLP) and Machine Learning.

The system combines Generative AI with a supervised text classification model to simulate and detect misinformation.

🧠 System Architecture

User Input
   ↓
Streamlit Web Interface
   ↓
 ┌──────────────────────────┐
 │  Fake News Generator     │ → LLM (Groq - Llama 3.1)
 └──────────────────────────┘
 ┌──────────────────────────┐
 │  Fake News Detector      │ → TF-IDF + LinearSVC
 └──────────────────────────┘
   ↓
Prediction Result Display

📂 Project Structure

FAKE-NEWS-AI-PROJECT/
│
├── data/
│   ├── True.csv
│   ├── Fake.csv
│   ├── combined.csv
│
├── models/
│   ├── fake_news_model.pkl
│   ├── vectorizer.pkl
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── combine_data.py
│   ├── train_model.py
│   ├── predict.py
│   ├── generator.py
│
├── app/
│   └── streamlit_app.py
│
├── requirements.txt
└── README.md

📊 Dataset

The model is trained on the:

Fake and Real News Dataset (Kaggle)

True.csv → Real news articles

Fake.csv → Fake news articles

Both datasets are combined and labeled:

0 → Real News

1 → Fake News

⚙️ Technologies Used

Python

Scikit-learn

TF-IDF Vectorization

LinearSVC / Logistic Regression

Streamlit

Groq API (Llama 3.1 model)

NLTK

Joblib

🧪 Model Details
🔹 Preprocessing

Lowercasing

Regex cleaning

Stopword removal (NLTK)

🔹 Feature Extraction

TF-IDF Vectorizer

N-grams (1,2)

🔹 Classification Model

LinearSVC (optimized for text classification)

📈 Training the Model

From project root:

python -m src.combine_data
python -m src.train_model

This will:

Merge datasets

Train the model

Save:

models/fake_news_model.pkl

models/vectorizer.pkl

🌐 Running the Application
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Set Groq API Key (Windows)
setx GROQ_API_KEY "your_api_key_here"
Restart terminal after setting.

3️⃣ Run Streamlit App
streamlit run app/streamlit_app.py

The app will open at:
http://localhost:8501

🔥 Features

Generate realistic fake news articles

Detect fake vs real news

Clean modular code structure

Package-based Python architecture

Scalable design

Resume-ready AI project
