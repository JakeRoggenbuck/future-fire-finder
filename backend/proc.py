import pandas as pd

df = pd.read_csv("./df6.csv")

# Add fire array to all items
df["fire"] = ["1"] * len(df)

df.to_csv("./df_fires.csv")
