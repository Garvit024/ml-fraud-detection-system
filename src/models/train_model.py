import os
import pandas as pd
from sqlalchemy import create_engine
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL not found")

MODEL_PATH = "ml_fraud_model.pkl"  # Railway will use project root

# -----------------------------
# Load data
# -----------------------------
engine = create_engine(DATABASE_URL)
df = pd.read_sql("SELECT * FROM feature_table", engine)

X = df[["amount","tx_count","avg_amt","merch_tx_count","fraud_rate"]]
y = df["is_fraud"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# -----------------------------
# Train model
# -----------------------------
model = XGBClassifier(
    n_estimators=300,
    max_depth=6,
    learning_rate=0.05,
    scale_pos_weight=20,
    eval_metric="logloss"
)

model.fit(X_train, y_train)

# -----------------------------
# Evaluate
# -----------------------------
print(classification_report(y_test, model.predict(X_test)))

# -----------------------------
# Save model
# -----------------------------
joblib.dump(model, MODEL_PATH)
print(f"✅ Model saved: {MODEL_PATH}")
