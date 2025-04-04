import sqlite3
import pandas as pd

db_file = "../db/superstore.db"
conn = sqlite3.connect(db_file)

# 1️⃣ Продажи по категориям
query = """
SELECT Category, SUM(Sales) as Total_Sales 
FROM sales 
GROUP BY Category
ORDER BY Total_Sales DESC
"""
df = pd.read_sql(query, conn)
print(df)

# 2️⃣ ТОП-10 клиентов по продажам
query = '''
SELECT "Customer Name", SUM(Sales) as Total_Sales 
FROM sales 
GROUP BY "Customer Name"
ORDER BY Total_Sales DESC
LIMIT 10
'''

df = pd.read_sql(query, conn)
print(df)

conn.close()
