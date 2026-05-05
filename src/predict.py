import joblib
from src.preprocessing import clean_text

model = joblib.load("models/fake_news_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_news(text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    prediction = model.predict(vec)[0]

    if prediction == 1:
        return "🚨 FAKE NEWS"
    else:
        return "✅ REAL NEWS"
