import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

# -----------------------------
# Load processed data
# -----------------------------
df = pd.read_csv("data/processed/transactions_processed.csv")

print("Data loaded:", df.shape)

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
y = df["is_fraud"]

# -----------------------------
# Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training size:", X_train.shape)
print("Testing size:", X_test.shape)

# -----------------------------
# Train model
# -----------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("Model trained successfully.")

# -----------------------------
# Evaluate model
# -----------------------------
y_pred = model.predict(X_test)

print("\nModel Evaluation:\n")
print(classification_report(y_test, y_pred))

# -----------------------------
# Save model
# -----------------------------
joblib.dump(model, "outputs/fraud_model.pkl")

print("\nModel saved to outputs/fraud_model.pkl")