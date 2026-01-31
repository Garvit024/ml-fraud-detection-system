import os
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "ml_fraud_model.pkl")

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load(MODEL_PATH)

# -----------------------------
# Define API
# -----------------------------
app = FastAPI(title="Fraud Detection API")

class Transaction(BaseModel):
    amount: float
    tx_count: int
    avg_amt: float
    merch_tx_count: int
    fraud_rate: float

@app.post("/predict")
def predict(tx: Transaction):
    df = pd.DataFrame([tx.dict()])
    pred = model.predict(df)[0]
    return {"is_fraud": int(pred)}
