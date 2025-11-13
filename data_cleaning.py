import pandas as pd
import html
import numpy as np
import re
#from os import display
#import sys
#sys.path.insert(0, "analysis/ena")
from data_cleaner_class import DataCleaner as dc

properties_data = pd.read_csv("./data/raw/data.csv")
#print(properties_data)

#remove duplicates
properties_data.drop_duplicates(subset=["Property ID"])
#print("ID")
#print(properties_data)

#remove no price, rent , private sale
#properties_data['Price'].replace('', None)
#properties_data['Price'].replace(' ', None)
properties_data['Price'].replace(r'^\s*$', np.nan, regex=True)#
properties_data.dropna(subset=['Price'])

discarded_properties = properties_data['Type of sale'].isin(['Rent', 'PublicSale', 'Share'])
properties_data = properties_data[~discarded_properties]

#print("rm")
#print(properties_data)


#fix the html encoding
properties_data['Locality name'] = properties_data['Locality name'].apply(lambda x: html.unescape(x))

#print('locality')
#print(properties_data)


#everything to int except property ID
#temp_properties_data = dc(properties_data)
properties_data = dc(properties_data).clean_all()

#properties_data['Garden Surface'] = properties_data['Garden'].copy()
#properties_data['Terrace Surface'] = properties_data['Terrace'].copy()

#pd.to_numeric(properties_data['Price'], errors='coerce').round().astype("Int64")



#print("clean")
#print(properties_data)


#remove empty spaces
properties_data.replace(r'^\s*$', None, regex=True)
#print("empty")
#print(properties_data)


#remove blank spaces from property ID
def rm_blank_spaces(column):
    id_column = properties_data[column]
    
    for row in id_column:
        if type(row) is str :
            #print(row)
            if row[0] == " ":
                row = row[1:]
            if row[-1] == " ":
                row = row[:-1]

rm_blank_spaces("Property ID")
rm_blank_spaces("Locality name")
rm_blank_spaces("Type of property")
rm_blank_spaces("State of building")

#print(properties_data.head())

properties_data.to_csv('clean_data.csv', index=False)