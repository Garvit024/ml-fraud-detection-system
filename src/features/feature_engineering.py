import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///db/fraud.db")

df = pd.read_sql("select * from raw_transactions", engine)

cust_stats = df.groupby("customer_id").agg(
    tx_count=("transaction_id","count"),
    avg_amt=("amount","mean")
).reset_index()

merch_stats = df.groupby("merchant_id").agg(
    merch_tx_count=("transaction_id","count"),
    fraud_rate=("is_fraud","mean")
).reset_index()

df = df.merge(cust_stats, on="customer_id")
df = df.merge(merch_stats, on="merchant_id")

df.to_sql("feature_table", engine, if_exists="replace", index=False)

print("✅ Features Created")
