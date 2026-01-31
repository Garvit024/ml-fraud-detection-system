import os
import pandas as pd
from sqlalchemy import create_engine
from faker import Faker
import numpy as np

fake = Faker()

# -----------------------------
# DB Setup
# -----------------------------
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///db/fraud.db")
engine = create_engine(DATABASE_URL)

# -----------------------------
# Generate fake data
# -----------------------------
N = 5000
data = {
    "amount": np.random.uniform(10, 1000, N),
    "tx_count": np.random.randint(1, 50, N),
    "avg_amt": np.random.uniform(10, 500, N),
    "merch_tx_count": np.random.randint(1, 30, N),
    "fraud_rate": np.random.uniform(0, 1, N),
    "is_fraud": np.random.choice([0, 1], N, p=[0.95, 0.05])
}

df = pd.DataFrame(data)

# -----------------------------
# Insert into DB
# -----------------------------
df.to_sql("feature_table", engine, if_exists="replace", index=False)
print(f"✅ Data Generated in {DATABASE_URL}")
