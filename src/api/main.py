import os
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from src.models.train_model import train_model

MODEL_PATH = "ml_fraud_model.pkl"

app = FastAPI(title="Fraud Detection API")

# Auto-load or train model
if not os.path.exists(MODEL_PATH):
    print("⚠ Model not found. Training new model...")
    train_model()
    print("✅ Model trained.")

model = joblib.load(MODEL_PATH)
print("✅ Model loaded successfully")

class Transaction(BaseModel):
    amount: float
    tx_count: int
    avg_amt: float
    merch_tx_count: int
    fraud_rate: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(tx: Transaction):
    df = pd.DataFrame([tx.dict()])
    prob = model.predict_proba(df)[0][1]
    return {
        "fraud_probability": round(float(prob), 4),
        "risk": "HIGH" if prob > 0.7 else "MEDIUM" if prob > 0.4 else "LOW"
    }
