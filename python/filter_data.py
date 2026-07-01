import pandas as pd

data = pd.read_csv("../Data/SampleSuperstore.csv")

consumer_data = data[data["Segment"] == "Consumer"]

print(consumer_data.head())