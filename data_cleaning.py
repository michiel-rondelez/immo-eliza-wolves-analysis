import pandas as pd
import html

properties_data = pd.read_csv("./data/raw/data.csv")

#fix the html encoding
properties_data['Locality name'] = properties_data['Locality name'].apply(lambda x: html.unescape(x))

#remove duplicates



#everything to int except property ID



#remove empty spaces



#remove blank spaces from property ID
def rm_blank_spaces():
    id_column = properties_data["Property ID"]
    for row in id_column:
        if row[0] == " ":
            row = row[1:]
        if row[-1] == " ":
            row = row[:-1]

