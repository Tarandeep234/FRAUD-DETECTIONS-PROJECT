import pandas as pd
import joblib

# -----------------------------
# Load processed data
# -----------------------------
df = pd.read_csv("data/processed/transactions_processed.csv")

# -----------------------------
# Load trained model
# -----------------------------
model = joblib.load("Outputs/fraud_model.pkl")

print("Model loaded successfully.")

# -----------------------------
# Select features
# -----------------------------
features = [
    "amount",
    "transaction_hour",
    "is_night",
    "is_high_amount",
    "is_online",
    "customer_avg_spend",
    "merchant_fraud_rate"
]

X = df[features]

# -----------------------------
# Predict probabilities and labels
# -----------------------------
df["fraud_probability"] = model.predict_proba(X)[:, 1]
df["predicted_fraud"] = model.predict(X)

# -----------------------------
# Save transaction-level predictions
# -----------------------------
predictions = df[
    [
        "transaction_id",
        "customer_id",
        "merchant_id",
        "amount",
        "fraud_probability",
        "predicted_fraud"
    ]
]

predictions.to_csv("Outputs/predictions.csv", index=False)

print("Predictions saved to outputs/predictions.csv")

# -----------------------------
# Create customer-level risk scores
# -----------------------------
risk_scores = df.groupby("customer_id").agg(
    avg_fraud_probability=("fraud_probability", "mean"),
    transaction_count=("transaction_id", "count"),
    fraud_flag_count=("predicted_fraud", "sum")
).reset_index()

# Simple risk score formula
risk_scores["risk_score"] = (
    risk_scores["avg_fraud_probability"] * 0.7 +
    (risk_scores["fraud_flag_count"] / risk_scores["transaction_count"]) * 0.3
)

risk_scores = risk_scores.sort_values(by="risk_score", ascending=False)

risk_scores.to_csv("Outputs/risk_scores.csv", index=False)

print("Risk scores saved to Outputs/risk_scores.csv")
print("\nTop risky customers:")
print(risk_scores.head(10))