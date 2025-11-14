import pandas as pd

df = pd.read_csv("./data/raw/data.csv", encoding='utf-8')

for row in df["Property ID"]:
    if row[0] == " ":
        row = row[1:]
    if row[-1] == " ":
        row = row[:-1]