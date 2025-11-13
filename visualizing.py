import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

properties_data = pd.read_csv("clean_data.csv") #change to clean data

#properties_data.apply(pd.Series.value_counts)
print(properties_data.info())
#properties_data.apply(pd.describe())


def histogram_for_nums(category : str):
    sns.histplot(data=properties_data, x=category) #do it for each num column
    plt.show()
"""
# visualize numerical columns
histogram_for_nums("Number of rooms")
histogram_for_nums("Living area")
histogram_for_nums("Terrace surface") #check spelling
histogram_for_nums("Garden Surface") # check spelling
"""