import pandas as pd

# Load datasets
true_df = pd.read_csv("True.csv")
fake_df = pd.read_csv("data/Fake.csv")

# Add labels
true_df["label"] = 0   # Real news
fake_df["label"] = 1   # Fake news

# Combine datasets
df = pd.concat([true_df, fake_df], axis=0)

# Keep only text + label
df = df[["text", "label"]]

# Shuffle dataset
df = df.sample(frac=1, random_state=42)

# Save combined file
df.to_csv("combined.csv", index=False)

print("✅ Combined dataset saved as combined.csv")
print("Total samples:", len(df))
