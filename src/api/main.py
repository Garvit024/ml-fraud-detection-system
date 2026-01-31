from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load your trained model
model = joblib.load("ml_fraud_model.pkl")

@app.get("/")
def root():
    return {"message": "Fraud Detection API is running!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: dict):

    X = np.array([[ 
        data["amount"],
        data["tx_count"],
        data["avg_amt"],
        data["merch_tx_count"],
        data["fraud_rate"]
    ]])

    prob = model.predict_proba(X)[0][1]

    return {
        "fraud_probability": float(prob),
        "risk": "HIGH" if prob > 0.7 else "LOW"
    }
