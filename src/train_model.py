import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from src.preprocessing import clean_text

# Load combined dataset
df = pd.read_csv("combined.csv")

# Clean text
df["text"] = df["text"].apply(clean_text)

X = df["text"]
y = df["label"]

# TF-IDF
vectorizer = TfidfVectorizer(
    max_features=15000,
    ngram_range=(1,2)   # adds bigrams
)

X = vectorizer.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearSVC()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("✅ Model Accuracy:", accuracy)

# Save model
joblib.dump(model, "models/fake_news_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("✅ Model & Vectorizer Saved!")
