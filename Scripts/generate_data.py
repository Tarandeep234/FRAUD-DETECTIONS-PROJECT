import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# -----------------------------
# Generate customers
# -----------------------------
num_customers = 200
customers = pd.DataFrame({
    "customer_id": [f"CUST{i:04d}" for i in range(1, num_customers + 1)],
    "age": np.random.randint(18, 70, num_customers),
    "country": np.random.choice(["UK", "US", "India", "Germany", "Canada"], num_customers),
    "account_age_days": np.random.randint(30, 3000, num_customers),
    "customer_segment": np.random.choice(["standard", "premium", "business"], num_customers)
})

# -----------------------------
# Generate merchants
# -----------------------------
num_merchants = 50
merchants = pd.DataFrame({
    "merchant_id": [f"MER{i:03d}" for i in range(1, num_merchants + 1)],
    "merchant_category": np.random.choice(
        ["electronics", "travel", "grocery", "fashion", "gaming", "utilities"],
        num_merchants
    ),
    "merchant_country": np.random.choice(["UK", "US", "India", "Germany", "Canada"], num_merchants)
})

# -----------------------------
# Generate transactions
# -----------------------------
num_transactions = 2000
start_date = datetime(2025, 1, 1)

transaction_times = [
    start_date + timedelta(minutes=int(np.random.randint(0, 60 * 24 * 180)))
    for _ in range(num_transactions)
]

transactions = pd.DataFrame({
    "transaction_id": [f"TXN{i:06d}" for i in range(1, num_transactions + 1)],
    "customer_id": np.random.choice(customers["customer_id"], num_transactions),
    "merchant_id": np.random.choice(merchants["merchant_id"], num_transactions),
    "transaction_time": transaction_times,
    "amount": np.round(np.random.exponential(scale=120, size=num_transactions), 2),
    "device_type": np.random.choice(["mobile", "web", "atm", "pos"], num_transactions),
    "channel": np.random.choice(["online", "card_present", "transfer"], num_transactions),
    "location": np.random.choice(["London", "Manchester", "Birmingham", "Leeds", "Glasgow"], num_transactions),
    "is_fraud": np.random.choice([0, 1], num_transactions, p=[0.94, 0.06])
})

# Add a few suspicious patterns to make the dataset more realistic
fraud_indices = transactions[transactions["is_fraud"] == 1].index

transactions.loc[fraud_indices, "amount"] = np.round(
    transactions.loc[fraud_indices, "amount"] * np.random.uniform(2.0, 5.0, len(fraud_indices)), 2
)
transactions.loc[fraud_indices, "channel"] = np.random.choice(["online", "transfer"], len(fraud_indices))
transactions.loc[fraud_indices, "device_type"] = np.random.choice(["mobile", "web"], len(fraud_indices))

# -----------------------------
# Save files
# -----------------------------
customers.to_csv("data/raw/customers.csv", index=False)
merchants.to_csv("data/raw/merchants.csv", index=False)
transactions.to_csv("data/raw/transactions.csv", index=False)

print("Raw datasets created successfully!")
print("Customers shape:", customers.shape)
print("Merchants shape:", merchants.shape)
print("Transactions shape:", transactions.shape)