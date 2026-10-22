import psycopg2
import pandas as pd
from psycopg2 import sql
import os

# ==== CONFIGURATION ====
HOST = "finane02.cjysyvncrayl.ap-south-1.rds.amazonaws.com"
PORT = 5432
USER = "postgres"
PASSWORD = "RDSdata123456"
DATABASE = "postgres"
CSV_PATH = r"C:\Ownership\Build Serverless Pipeline using AWS CDK and Lambda in Python\stock_data_historical.csv"
SCHEMA = "finance"
TABLE = "stock_data_historical"

# ==== STEP 1: Connect to PostgreSQL ====
conn = psycopg2.connect(
    host=HOST,
    port=PORT,
    user=USER,
    password=PASSWORD,
    database=DATABASE
)
cursor = conn.cursor()

# ==== STEP 2: Create schema if not exists ====
cursor.execute(sql.SQL("CREATE SCHEMA IF NOT EXISTS {}").format(sql.Identifier(SCHEMA)))
conn.commit()

# ==== STEP 3: Read CSV and create table ====
df = pd.read_csv(CSV_PATH)

columns_with_types = ", ".join([f'"{col}" TEXT' for col in df.columns])
create_table_query = sql.SQL("""
    CREATE TABLE IF NOT EXISTS {}.{} (
        {}
    )
""").format(
    sql.Identifier(SCHEMA),
    sql.Identifier(TABLE),
    sql.SQL(columns_with_types)
)
cursor.execute(create_table_query)
conn.commit()

# ==== STEP 4: Insert CSV data into table ====
temp_csv_path = "temp_upload.csv"
df.to_csv(temp_csv_path, index=False, header=False)

with open(temp_csv_path, 'r') as f:
    cursor.copy_expert(
        f"COPY {SCHEMA}.{TABLE} FROM STDIN WITH CSV",
        f
    )
conn.commit()

# ==== Cleanup ====
cursor.close()
conn.close()
os.remove(temp_csv_path)  # optional cleanup

print(f"Uploaded {len(df)} rows to {SCHEMA}.{TABLE} in database {DATABASE}")
