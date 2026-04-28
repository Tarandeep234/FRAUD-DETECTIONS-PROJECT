@echo off
echo ===============================
echo FRAUD DETECTION PIPELINE START
echo ===============================

echo.
echo [1/7] Generating raw data...
python scripts/generate_data.py

echo.
echo [2/7] Validating data...
python scripts/validate_data.py

echo.
echo [3/7] Engineering features...
python scripts/feature_engineering.py

echo.
echo [4/7] Training fraud model...
python scripts/train_model.py

echo.
echo [5/7] Scoring transactions...
python scripts/score_transactions.py

echo.
echo [6/7] Loading data into SQL...
python scripts/load_data_to_sql.py

echo.
echo [7/7] Running analytics queries...
python scripts/run_analytics.py

echo.
echo ===============================
echo PIPELINE COMPLETED SUCCESSFULLY
echo ===============================
pause