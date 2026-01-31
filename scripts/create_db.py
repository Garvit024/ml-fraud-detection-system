import sqlite3
import pandas as pd
from faker import Faker
import random
import os

DB_PATH = os.path.join("db", "fraud.db")
conn = sqlite3.connect(DB_PATH)

fake = Faker()
rows = []
for _ in range(10000):
    amount = round(random.uniform(10, 5000), 2)
    tx_count = random.randint(1, 10)
    avg_amt = round(random.uniform(10, 3000), 2)
    merch_tx_count = random.randint(1, 100)
    fraud_rate = round(random.uniform(0, 0.1), 4)
    is_fraud = random.choices([0,1], weights=[0.97,0.03])[0]
    rows.append((amount, tx_count, avg_amt, merch_tx_count, fraud_rate, is_fraud))

df = pd.DataFrame(rows, columns=["amount","tx_count","avg_amt","merch_tx_count","fraud_rate","is_fraud"])
df.to_sql("feature_table", conn, if_exists="replace", index=False)

conn.close()
print("✅ Dummy data inserted into feature_table")
