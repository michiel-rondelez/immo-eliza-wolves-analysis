import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 

properties_data = pd.read_csv("clean_data_0.csv")
threshold = properties_data["Price"].quantile(0.90)
properties_data = properties_data[properties_data["Price"]<= threshold.astype(int)]

sns.scatterplot(
    x="Garden Surface",
    y="Price", 
    data=properties_data[properties_data["Garden Surface"]<= 10000],
    palette='Pastel2')



plt.tight_layout()
plt.show()