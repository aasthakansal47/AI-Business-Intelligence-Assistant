import pandas as pd
data = pd.read_csv("../Data/SampleSuperstore.csv")
print(" First 5 rows : ")
print (data.head())
print("\n Number of rows and columns :")
print(data.shape)
print("\nColumn Names:")
print(data.columns)

print("Total Sales:")
print(data["Sales"].sum())
print("Total Profit:")
print(data["Profit"].sum())
print("Total Quantity:")
print(data["Quantity"].sum())

print("AVG : ")
print(data["Sales"].mean())
print("\n max and min : ")
print(data["Profit"].max())
print(data["Discount"].min())

print("Show me the total quantity of products sold.")
print(data["Quantity"].sum())