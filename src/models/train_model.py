import pandas as pd
from sqlalchemy import create_engine
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

engine = create_engine("sqlite:///db/fraud.db")

df = pd.read_sql("select * from feature_table", engine)

X = df[["amount","tx_count","avg_amt","merch_tx_count","fraud_rate"]]
y = df["is_fraud"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

model = XGBClassifier(
    n_estimators=300,
    max_depth=6,
    learning_rate=0.05,
    scale_pos_weight=20,
    eval_metric="logloss"
)

model.fit(X_train, y_train)

print(classification_report(y_test, model.predict(X_test)))

joblib.dump(model, "ml_fraud_model.pkl")
print("✅ Model Trained & Saved")
