import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

properties_data = pd.read_csv("clean_data_0.csv") #change to clean data

properties_data.boxplot(by="Subtype of property", column=)