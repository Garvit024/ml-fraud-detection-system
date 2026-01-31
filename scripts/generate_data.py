import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
np.random.seed(42)

N = 50000

customers = [f"C{i}" for i in range(1000)]
merchants = [f"M{i}" for i in range(200)]

data = []

for i in range(N):
    cust = random.choice(customers)
    merch = random.choice(merchants)
    amt = round(np.random.exponential(2000), 2)
    fraud = 1 if random.random() < 0.03 else 0

    data.append([
        f"TX{i}", cust, merch, amt,
        fake.latitude(), fake.longitude(), fraud
    ])

df = pd.DataFrame(data, columns=[
    "transaction_id","customer_id","merchant_id",
    "amount","lat","lon","is_fraud"
])

df.to_csv("data/raw/transactions.csv", index=False)
print("✅ Data Generated")
