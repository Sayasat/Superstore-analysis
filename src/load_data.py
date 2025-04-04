import pandas as pd
import sqlite3

csv_file = "../data/superstore.csv"
db_file = "../db/superstore.db"

df = pd.read_csv(csv_file, encoding="ISO-8859-1")
conn = sqlite3.connect(db_file)

# Сохраняем в таблицу sales
df.to_sql("sales", conn, if_exists="replace", index=False)

conn.close()
