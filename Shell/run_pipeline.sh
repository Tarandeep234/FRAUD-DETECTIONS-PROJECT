#!/bin/bash

echo "==============================="
echo "FRAUD DETECTION PIPELINE START"
echo "==============================="

python scripts/generate_data.py
python scripts/validate_data.py
python scripts/feature_engineering.py
python scripts/train_model.py
python scripts/score_transactions.py
python scripts/load_data_to_sql.py
python scripts/run_analytics.py

echo "==============================="
echo "PIPELINE COMPLETED SUCCESSFULLY"
echo "==============================="