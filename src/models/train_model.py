import os
import sys
import pandas as pd
from sqlalchemy import create_engine
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# -----------------------------
# Paths
# -----------------------------
# Get project root (fraud-detection-local)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_PATH = os.path.join(BASE_DIR, "db", "fraud.db")
MODEL_PATH = os.path.join(BASE_DIR, "ml_fraud_model.pkl")

# -----------------------------
# Check if DB exists
# -----------------------------
if not os.path.exists(DB_PATH):
    print(f"❌ Database not found: {DB_PATH}")
    sys.exit(1)

# -----------------------------
# Load features from SQLite
# -----------------------------
try:
    engine = create_engine(f"sqlite:///{DB_PATH}")
    df = pd.read_sql("SELECT * FROM feature_table", engine)
except Exception as e:
    print(f"❌ Error reading from DB: {e}")
    sys.exit(1)

# -----------------------------
# Prepare data
# -----------------------------
X = df[["amount", "tx_count", "avg_amt", "merch_tx_count", "fraud_rate"]]
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
try:
    joblib.dump(model, MODEL_PATH)
    print(f"✅ Model Trained & Saved: {MODEL_PATH}")
except Exception as e:
    print(f"❌ Error saving model: {e}")
