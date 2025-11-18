import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 


def remove_outliers(group, column):
    Q1 = group[column].quantile(0.25)
    Q3 = group[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return group[(group[column] >= lower) & (group[column] <= upper)]

properties_data = pd.read_csv("clean_data_0.csv") #change to clean data
threshold = properties_data["Price per m2"].quantile(0.90)
properties_data = properties_data[properties_data["Price per m2"]<= threshold.astype(int)]
#properties_data = remove_outliers(properties_data, "Number of rooms")[(properties_data["Price per m2"]<= threshold.astype(int)) & (properties_data["Type of property"] == "Appartment")]
#print(properties_data.head())

#visual for price/m2/subtype, Price/m2 cutoff#################################################################################################
#fig, ax1 = plt.subplots()
order = properties_data.groupby("Subtype of property")["Price per m2"].median().sort_values().index
#threshold = properties_data["Price per m2"].quantile(0.90)
my_box = sns.boxplot(
    x="Subtype of property",
    y="Price per m2", 
    data=properties_data,#[properties_data["Price per m2"]<= threshold.astype(int)], 
    order=order, 
    palette='Set3', 
    #ax=ax1
    )
#ax1.set_ylabel("Price per m² (€)")
my_box.set(xlabel ="Property Subtype", ylabel = "Price per m² (€)", title ='Price per m² per property subtype')
sns.set_style("whitegrid")
plt.axhline(properties_data["Price per m2"].median(), color='purple', linestyle='-', linewidth=1)
#plt.yscale('log')
"""
#Add median living area per subtypes
median_area = properties_data.groupby("Subtype of property")["Number of rooms"].median().sort_values()
x_positions = range(len(median_area))

ax2 = ax1.twinx()
ax2.plot(x_positions, median_area.values, color="red", marker="o", linewidth=0)
#ax2.plot(x_positions, median_area["House"], color="red", marker="o", linewidth=1)
#ax2.plot(x_positions, median_area["Appartment"], color="blue", marker="o", linewidth=1)
#ax2.set_ylabel("Median living area (m²)", color="red")
ax2.set_xticks(x_positions)
ax2.set_xticklabels(median_area.index, rotation=45, ha="right")
"""
plt.tight_layout()
plt.show()