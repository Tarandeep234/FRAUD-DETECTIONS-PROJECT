import sqlite3
import pandas as pd
from pathlib import Path

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "fraud.db"
output_dir = BASE_DIR / "Outputs"

# -----------------------------
# Connect to database
# -----------------------------
conn = sqlite3.connect(db_path)
print(f"Connected to database: {db_path}")

# -----------------------------
# Query 1: Fraud rate by country
# -----------------------------
query1 = """
SELECT
    c.country,
    COUNT(t.transaction_id) AS total_transactions,
    SUM(t.is_fraud) AS fraud_transactions,
    ROUND(CAST(SUM(t.is_fraud) AS REAL) / COUNT(t.transaction_id), 4) AS fraud_rate
FROM transactions t
JOIN customers c
    ON t.customer_id = c.customer_id
GROUP BY c.country
ORDER BY fraud_rate DESC;
"""

fraud_by_country = pd.read_sql_query(query1, conn)
fraud_by_country.to_csv(output_dir / "fraud_by_country.csv", index=False)

# -----------------------------
# Query 2: Fraud rate by channel
# -----------------------------
query2 = """
SELECT
    channel,
    COUNT(*) AS total_transactions,
    SUM(is_fraud) AS fraud_transactions,
    ROUND(CAST(SUM(is_fraud) AS REAL) / COUNT(*), 4) AS fraud_rate
FROM transactions
GROUP BY channel
ORDER BY fraud_rate DESC;
"""

fraud_by_channel = pd.read_sql_query(query2, conn)
fraud_by_channel.to_csv(output_dir / "fraud_by_channel.csv", index=False)

# -----------------------------
# Query 3: Top risky customers
# -----------------------------
query3 = """
SELECT
    customer_id,
    avg_fraud_probability,
    transaction_count,
    fraud_flag_count,
    risk_score
FROM risk_scores
ORDER BY risk_score DESC
LIMIT 20;
"""

top_risky_customers = pd.read_sql_query(query3, conn)
top_risky_customers.to_csv(output_dir / "top_risky_customers.csv", index=False)

# -----------------------------
# Query 4: Top risky merchants
# -----------------------------
query4 = """
SELECT
    merchant_id,
    COUNT(*) AS total_transactions,
    SUM(is_fraud) AS fraud_transactions,
    ROUND(CAST(SUM(is_fraud) AS REAL) / COUNT(*), 4) AS fraud_rate
FROM transactions
GROUP BY merchant_id
ORDER BY fraud_rate DESC
LIMIT 20;
"""

top_risky_merchants = pd.read_sql_query(query4, conn)
top_risky_merchants.to_csv(output_dir / "top_risky_merchants.csv", index=False)

print("Analytics outputs created successfully.")

# -----------------------------
# Close connection
# -----------------------------
conn.close()
print("Database connection closed.")