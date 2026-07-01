import pandas as pd

data = pd.read_csv("../Data/SampleSuperstore.csv")

region_sales = data.groupby("Region")["Sales"].sum()

print(region_sales)

# calculate total profit for each region
# data.groupby("Region")["Profit"].sum()
# How would you calculate Total Sales for each Category?
# data.groupby("Category")["Sales"].sum()