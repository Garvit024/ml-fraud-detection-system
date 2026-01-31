import os
from sqlalchemy import create_engine, text

# Get DB URL from env (Railway)
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///db/fraud.db")
engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS feature_table (
            id SERIAL PRIMARY KEY,
            amount FLOAT,
            tx_count INT,
            avg_amt FLOAT,
            merch_tx_count INT,
            fraud_rate FLOAT,
            is_fraud INT
        )
    """))
    conn.commit()

print(f"✅ DB and table created: {DATABASE_URL}")
