import sqlite3
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Files
db_path = BASE_DIR / "fraud.db"
schema_path = BASE_DIR / "sql" / "schema.sql"

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print(f"Connected to database: {db_path}")

# Read schema
with open(schema_path, "r", encoding="utf-8") as f:
    sql_script = f.read()

# Convert Oracle-style types to SQLite-friendly types
sql_script = sql_script.replace("VARCHAR2(20)", "TEXT")
sql_script = sql_script.replace("VARCHAR2(50)", "TEXT")
sql_script = sql_script.replace("VARCHAR2(100)", "TEXT")
sql_script = sql_script.replace("NUMBER(10,2)", "REAL")
sql_script = sql_script.replace("NUMBER(10,4)", "REAL")
sql_script = sql_script.replace("NUMBER(1)", "INTEGER")
sql_script = sql_script.replace("NUMBER", "INTEGER")
sql_script = sql_script.replace("TIMESTAMP", "TEXT")

# Execute schema
cursor.executescript(sql_script)

conn.commit()
conn.close()

print("Tables created successfully in fraud.db")