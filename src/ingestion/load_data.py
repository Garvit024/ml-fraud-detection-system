import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///db/fraud.db")

df = pd.read_csv("data/raw/transactions.csv")
df.to_sql("raw_transactions", engine, if_exists="replace", index=False)

print("✅ Data loaded into SQLite")

