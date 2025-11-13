import pandas as pd

df = pd.read_csv("./data/raw/data.csv")

id_column = df["Property ID"]

for row in id_column:
    if row[0] == " ":
        row = row[1:]
    if row[-1] == " ":
        row = row[:-1]

    
