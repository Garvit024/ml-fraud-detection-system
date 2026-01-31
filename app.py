from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

MODEL_PATH = "ml_fraud_model.pkl"
model = joblib.load(MODEL_PATH)

@app.get("/")
def root():
    return {"message": "Fraud Detection API running!"}

@app.post("/predict")
def predict(transaction: dict):
    df = pd.DataFrame([transaction])
    pred = model.predict(df)[0]
    return {"is_fraud": int(pred)}
