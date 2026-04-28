import sqlite3
import pandas as pd
from pathlib import Path

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "fraud.db"

# Input CSVs
customers_path = BASE_DIR / "data" / "validated" / "customers_validated.csv"
merchants_path = BASE_DIR / "data" / "validated" / "merchants_validated.csv"
transactions_path = BASE_DIR / "data" / "validated" / "transactions_validated.csv"
predictions_path = BASE_DIR / "Outputs" / "predictions.csv"
risk_scores_path = BASE_DIR / "Outputs" / "risk_scores.csv"

# -----------------------------
# Connect to database
# -----------------------------
conn = sqlite3.connect(db_path)

print(f"Connected to database: {db_path}")

# -----------------------------
# Load CSV files
# -----------------------------
customers = pd.read_csv(customers_path)
merchants = pd.read_csv(merchants_path)
transactions = pd.read_csv(transactions_path)
predictions = pd.read_csv(predictions_path)
risk_scores = pd.read_csv(risk_scores_path)

print("CSV files loaded successfully.")

# -----------------------------
# Write to database tables
# -----------------------------
customers.to_sql("customers", conn, if_exists="replace", index=False)
merchants.to_sql("merchants", conn, if_exists="replace", index=False)
transactions.to_sql("transactions", conn, if_exists="replace", index=False)
predictions.to_sql("predictions", conn, if_exists="replace", index=False)
risk_scores.to_sql("risk_scores", conn, if_exists="replace", index=False)

print("All tables loaded into SQLite successfully.")

# -----------------------------
# Close connection
# -----------------------------
conn.close()
print("Database connection closed.")