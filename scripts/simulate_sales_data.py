import pandas as pd
import random
import numpy as np
from datetime import datetime

start_date = datetime(2025, 3, 1)
end_date = datetime(2025, 8, 1)
locations = ["Loop", "Wicker Park", "Hyde Park"]
products = [
    {"name": "Latte", "price": 4.5},
    {"name": "Cold Brew", "price": 5.0},
    {"name": "Croissant", "price": 3.0},
    {"name": "Muffin", "price": 2.5}
]
hours = list(range(7, 20))
dates = pd.date_range(start=start_date, end=end_date)
rows = []

for date in dates:
    for hour in hours:
        for location in locations:
            if location == "Loop":
                transactions = random.randint(6, 10)
            elif location == "Wicker Park":
                transactions = random.randint(3, 6)
            else:
                transactions = random.randint(2, 4)
            for _ in range(transactions):
                product = random.choices(
                    population=products,
                    weights=[0.4, 0.3, 0.2, 0.1],
                    k=1
                )[0]
                quantity = random.randint(1, 3)
                rows.append([
                    date.strftime("%Y-%m-%d"),
                    f"{hour}:00",
                    location,
                    product["name"],
                    product["price"],
                    quantity,
                    f"C{random.randint(1000, 9999)}",
                    random.choice(["Card", "Cash"])
                ])

df = pd.DataFrame(rows, columns=["Date", "Time", "Location", "Product", "Price", "Quantity", "Customer_ID", "Payment_Type"])
df["Date"] = pd.to_datetime(df["Date"])
df["Revenue"] = df["Price"] * df["Quantity"]

np.random.seed(42)
inventory_levels = {
    "Loop": list(np.random.normal(loc=300, scale=25, size=len(df[df["Location"] == "Loop"]))),
    "Wicker Park": list(np.random.normal(loc=200, scale=20, size=len(df[df["Location"] == "Wicker Park"]))),
    "Hyde Park": list(np.random.normal(loc=150, scale=15, size=len(df[df["Location"] == "Hyde Park"])))
}

df["inventory_level"] = df.apply(lambda row: inventory_levels[row["Location"]].pop(), axis=1)

df.to_csv("data/coffee_sales.csv", index=False)
print("offee_sales.csv saved.")