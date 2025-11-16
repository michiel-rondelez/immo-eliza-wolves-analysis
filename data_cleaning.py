import pandas as pd
import html
import numpy as np
import re
#from os import display
#import sys
#sys.path.insert(0, "analysis/ena")
from data_cleaner_class import DataCleaner as dc

properties_data = pd.read_csv("./data/raw/data.csv")
#print(properties_data.head(10))

#remove duplicates###########################################################################################################
properties_data.drop_duplicates(subset=["Property ID"])
#print("ID")
print(properties_data.columns)

#remove price, rent , private sale, share + houses where price = 0 ######################################################################################
properties_data['Price'].replace(r'^\s*$|^0.00$', np.nan, regex=True)#
properties_data.dropna(subset=['Price'])
discarded_properties = properties_data['Price'].isin([None, 0, 0.00, '0.00'])
properties_data = properties_data[~discarded_properties]
bool_price = pd.notnull(properties_data['Price'])
count = 0
for b in bool_price:
    if not b:
        print(b)
properties_data = properties_data[bool_price]



discarded_properties = properties_data['Type of sale'].isin(['Rent', 'PublicSale', 'Share'])
properties_data = properties_data[~discarded_properties]

#print("rm")
#print(properties_data)

#droping sales column as there's only one option left#########################################################################
#properties_data.drop('Type of sale', axis=1)

properties_data = properties_data.drop(columns=['Type of sale'])
print()
print("Check if the column 'Type of sale' has been deleted")
print()
print(properties_data.columns)



#fix the html encoding####################################################################################################
properties_data['Locality name'] = properties_data['Locality name'].apply(lambda x: html.unescape(x))

#print('locality')
#print(properties_data)


#everything to int except property ID###################################################################################
properties_data = dc(properties_data).clean_all()

#properties_data['Garden Surface'] = properties_data['Garden'].copy()
#properties_data['Terrace Surface'] = properties_data['Terrace'].copy()

#pd.to_numeric(properties_data['Price'], errors='coerce').round().astype("Int64")



#print("clean")
#print(properties_data)


#replace nones and equivalents#################################################################################################
properties_data[properties_data.select_dtypes(exclude=np.number).columns] = (properties_data[properties_data.select_dtypes(exclude=np.number).columns].replace({pd.NA: 'Unknown', None: 'Unknown', np.nan: 'Unknown'}).fillna('Unknown')) #replacing nones with "unknown" to avoid conflicts
properties_data[["Garden", "Terrace", "Equipped kitchen", "Open fire", "Swimming pool"]].fillna(0, inplace=True)

#print(properties_data.select_dtypes(exclude=np.number).head(11))
#print(properties_data[["Garden", "Terrace", "Equipped kitchen", "Open fire", "Swimming pool"]].head(11))


#remove empty spaces#######################################################################################################
properties_data.replace(r'^\s*$', None, regex=True)
#print("empty")
#print(properties_data)


#remove blank spaces from strings########################################################################################
def rm_blank_spaces(column):
    id_column = properties_data[column]
    
    for row in id_column:
        if type(row) is str :
            #print(row)
            if row[0] == " ":
                row = row[1:]
            if row[-1] == " ":
                row = row[:-1]

for column in properties_data.select_dtypes(exclude=np.number).columns:
    rm_blank_spaces(column)
#print("end", properties_data.head())

properties_data.to_csv('clean_data_0.csv', index=False)