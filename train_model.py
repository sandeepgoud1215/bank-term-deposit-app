import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Load dataset
df = pd.read_csv("bankmarketing.csv")

# ✅ Drop 'duration' to avoid data leakage
if 'duration' in df.columns:
    df = df.drop(columns=['duration'])

# Encode categorical variables
label_encoders = {}
categorical_cols = df.select_dtypes(include=['object']).columns

for col in categorical_cols:
    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(df[col])
    label_encoders[col] = encoder

# Features and target
X = df.drop("y", axis=1)
y = df["y"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and encoders
joblib.dump(model, "random_forest_model.pkl")
joblib.dump(X.columns.tolist(), "feature_names.pkl")
joblib.dump(label_encoders, "label_encoders.pkl")

print("✅ Model training complete and files saved:")
print("- random_forest_model.pkl")
print("- feature_names.pkl")
print("- label_encoders.pkl")
