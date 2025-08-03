import pandas as pd
import sqlite3
import os

csv_path = os.path.join("data", "coffee_sales.csv")
df = pd.read_csv(csv_path)

db_path = os.path.join("data", "cozy_bean.db")
connect = sqlite3.connect(db_path)

df.to_sql("sales", connect, if_exists="replace", index=False)

print("Loaded coffee_sales.csv ")
