import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 

def visual_sub_price_surface(type_property):
    properties_data = pd.read_csv("clean_data_0.csv")
    properties_data = properties_data[properties_data["Type of property"] == type_property].copy()
    threshold = properties_data["Price per m2"].quantile(0.90)
    properties_data = properties_data[properties_data["Price per m2"]<= threshold.astype(int)]

    order = properties_data.groupby("Subtype of property")["Price per m2"].median().sort_values().index
    my_box = sns.boxplot(
        x="Subtype of property",
        y="Price per m2", 
        data=properties_data,
        order=order, 
        palette='Set3'
        )

    my_box.set(xlabel ="Property Subtype", ylabel = "Price per m² (€)", title = F'Price per m² per property subtype ({type_property})')
    #sns.set_style("whitegrid")
    plt.axhline(properties_data["Price per m2"].median(), color='purple', linestyle='-', linewidth=1)
    plt.tight_layout()
    plt.show()

visual_sub_price_surface("House")
visual_sub_price_surface("Appartment")