import pandas as pd

# -----------------------------
# Load validated datasets
# -----------------------------
customers = pd.read_csv("data/validated/customers_validated.csv")
merchants = pd.read_csv("data/validated/merchants_validated.csv")
transactions = pd.read_csv("data/validated/transactions_validated.csv")

print("Datasets loaded.")

# -----------------------------
# Convert transaction_time
# -----------------------------
transactions["transaction_time"] = pd.to_datetime(transactions["transaction_time"])

# -----------------------------
# Feature 1: Transaction Hour
# -----------------------------
transactions["transaction_hour"] = transactions["transaction_time"].dt.hour

# -----------------------------
# Feature 2: Night transaction flag
# -----------------------------
transactions["is_night"] = transactions["transaction_hour"].apply(
    lambda x: 1 if x >= 22 or x <= 5 else 0
)

# -----------------------------
# Feature 3: High amount flag
# -----------------------------
threshold = transactions["amount"].quantile(0.90)
transactions["is_high_amount"] = transactions["amount"].apply(
    lambda x: 1 if x > threshold else 0
)

# -----------------------------
# Feature 4: Online transaction flag
# -----------------------------
transactions["is_online"] = transactions["channel"].apply(
    lambda x: 1 if x == "online" else 0
)

# -----------------------------
# Feature 5: Customer average spend
# -----------------------------
customer_avg = transactions.groupby("customer_id")["amount"].mean().reset_index()
customer_avg.rename(columns={"amount": "customer_avg_spend"}, inplace=True)

transactions = transactions.merge(customer_avg, on="customer_id", how="left")

# -----------------------------
# Feature 6: Merchant fraud rate
# -----------------------------
merchant_fraud = transactions.groupby("merchant_id")["is_fraud"].mean().reset_index()
merchant_fraud.rename(columns={"is_fraud": "merchant_fraud_rate"}, inplace=True)

transactions = transactions.merge(merchant_fraud, on="merchant_id", how="left")

# -----------------------------
# Save processed dataset
# -----------------------------
transactions.to_csv("data/processed/transactions_processed.csv", index=False)

print("Feature engineering complete!")
print("Processed dataset shape:", transactions.shape)