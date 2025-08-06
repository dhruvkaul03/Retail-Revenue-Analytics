import pandas as pd

df = pd.read_csv("data/coffee_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Week"] = df["Date"].dt.to_period("W")

weekly = df.groupby(["Week", "Location"]).agg(
    total_revenue=("Revenue", "sum"),
    avg_inventory=("inventory_level", "mean")
).reset_index()

weekly["pct_change"] = weekly.groupby("Location")["total_revenue"].pct_change()
weekly["flagged"] = weekly["pct_change"] <= -0.10

print(weekly[weekly["flagged"]])
