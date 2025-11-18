import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

properties_data = pd.read_csv("clean_data_0.csv") #change to clean data

#print(properties_data.info())
"""
for col in properties_data:
    properties_data[col].value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True).to_csv(f"overview/value_counts_{col}.csv")
"""
#print(properties_data.select_dtypes(exclude=np.number).apply(pd.Series.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)))


#properties_data.apply(pd.Series.describe).to_csv('describe.csv', index=False)

def histogram_for_nums(category : str):
    sns.histplot(data=properties_data, x=category) #do it for each num column
    plt.show()

# visualize numerical columns
#histogram_for_nums("Number of rooms")
histogram_for_nums("Living area")
#histogram_for_nums("Terrace Surface") #check spelling
#histogram_for_nums("Garden Surface") # check spelling#
#histogram_for_nums("Price")
#histogram_for_nums("Type of property")
#histogram_for_nums('Subtype of property')
#print(properties_data["Price"].corr(properties_data["Living area"]))

#print(properties_data.select_dtypes(include=np.number).columns)
for column in properties_data.select_dtypes(include=np.number).columns:
    #if column != "Property ID":
    for column_comp in properties_data.select_dtypes(include=np.number).columns:
            #if column_comp != "Property ID":
        print(f"corr {column} - {column_comp} : {properties_data[column].corr(properties_data[column_comp])}")
