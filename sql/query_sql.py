import pandas as pd
import sqlite3

connect = sqlite3.connect("data/cozy_bean.db")

query_1 = '''
SELECT Location, ROUND(SUM(Price * Quantity), 2) AS Total_Revenue
FROM sales
GROUP BY Location
ORDER BY Total_Revenue DESC;
'''

query_2 = '''
SELECT Product, SUM(Quantity) AS Units_Sold
FROM sales
GROUP BY Product
ORDER BY Units_Sold DESC
LIMIT 5;
'''

query_3 = '''
SELECT Time, SUM(Price * Quantity) AS Hourly_Revenue
FROM sales
GROUP BY Time
ORDER BY Time;
'''

df_1 = pd.read_sql(query_1, connect)
df_2 = pd.read_sql(query_2, connect)
df_3 = pd.read_sql(query_3, connect)

print("Revenue by Location:")
print(df_1)

print("Top 5 Selling Products:")
print(df_2)

print("Hourly Revenue:")
print(df_3)