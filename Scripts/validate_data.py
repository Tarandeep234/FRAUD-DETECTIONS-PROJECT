import pandas as pd

# -----------------------------
# Load raw datasets
# -----------------------------
customers = pd.read_csv("data/raw/customers.csv")
merchants = pd.read_csv("data/raw/merchants.csv")
transactions = pd.read_csv("data/raw/transactions.csv")

print("Datasets loaded successfully.")
print("Customers:", customers.shape)
print("Merchants:", merchants.shape)
print("Transactions:", transactions.shape)

# -----------------------------
# CUSTOMER VALIDATION
# -----------------------------
print("\n--- CUSTOMER VALIDATION ---")

print("Missing values in customers:")
print(customers.isnull().sum())

print("\nDuplicate customer_id count:")
print(customers["customer_id"].duplicated().sum())

# Remove duplicate customer IDs if any
customers = customers.drop_duplicates(subset=["customer_id"])

# Filter invalid ages
customers = customers[(customers["age"] >= 18) & (customers["age"] <= 100)]

# Filter invalid account age
customers = customers[customers["account_age_days"] >= 0]

print("Validated customers shape:", customers.shape)

# -----------------------------
# MERCHANT VALIDATION
# -----------------------------
print("\n--- MERCHANT VALIDATION ---")

print("Missing values in merchants:")
print(merchants.isnull().sum())

print("\nDuplicate merchant_id count:")
print(merchants["merchant_id"].duplicated().sum())

# Remove duplicate merchant IDs if any
merchants = merchants.drop_duplicates(subset=["merchant_id"])

print("Validated merchants shape:", merchants.shape)

# -----------------------------
# TRANSACTION VALIDATION
# -----------------------------
print("\n--- TRANSACTION VALIDATION ---")

print("Missing values in transactions:")
print(transactions.isnull().sum())

print("\nDuplicate transaction_id count:")
print(transactions["transaction_id"].duplicated().sum())

# Remove duplicate transactions
transactions = transactions.drop_duplicates(subset=["transaction_id"])

# Remove invalid amounts
transactions = transactions[transactions["amount"] > 0]

# Keep only valid fraud labels
transactions = transactions[transactions["is_fraud"].isin([0, 1])]

# Convert transaction_time to datetime
transactions["transaction_time"] = pd.to_datetime(
    transactions["transaction_time"],
    errors="coerce"
)

# Remove rows where transaction_time could not be parsed
transactions = transactions.dropna(subset=["transaction_time"])

# Check valid customer and merchant references
transactions = transactions[
    transactions["customer_id"].isin(customers["customer_id"])
]

transactions = transactions[
    transactions["merchant_id"].isin(merchants["merchant_id"])
]

print("Validated transactions shape:", transactions.shape)

# -----------------------------
# Save validated datasets
# -----------------------------
customers.to_csv("data/validated/customers_validated.csv", index=False)
merchants.to_csv("data/validated/merchants_validated.csv", index=False)
transactions.to_csv("data/validated/transactions_validated.csv", index=False)

print("\nValidated datasets saved successfully!")