#__________________ Data Cleaning with Class __________________#
import pandas as pd
import os
import html
import re
import os

# Load CSV
#file_path = "data/raw/data.csv"
#print("File exists:", os.path.exists(file_path))
#df = pd.read_csv(file_path)


# Define the DataCleaner class
class DataCleaner:
    def __init__(self, df):
        self.df = df.copy()
        # Rename columns to standard names if needed
        #self.df.rename(columns={
        #    "Garden": "Garden Surface",
        #    "Terrace": "Terrace Surface"
       # })

        # Duplicate Garden Surface and Terrace Surface to new columns Garden and Terrace
        self.df['Garden Surface'] = df['Garden'].copy()
        self.df['Terrace Surface'] = df['Terrace'].copy()


    #Convert True/False/NA to integers (1/0).
    def clean_boolean_column(self,x):
        if pd.isna(x):
           return 0
        x_str = str(x).strip().lower()
        if x_str in ["true", "1", "yes"]:
           return 1
        elif x_str in ["false", "0", "no"]:
             return 0
        else:
            return 0

    # Clean Price column
    def clean_price(self):
        self.df['Price'] = pd.to_numeric(self.df['Price'], errors='coerce').round().astype("Int64")

    # Clean Type of property
    def clean_property_type(self):
        mapping = {'house': 1, 'apartment': 0, 'flat': 0, 'villa': 1}
        self.df['Type of property'] = self.df['Type of property'].apply(
            lambda x: mapping.get(str(x).strip().lower(), None)
        ).astype("Int64")

    # Clean Garden and Terrace (1 if True or any number, 0 if False or empty)
    def clean_garden_terrace(self):
        def helper(x):
            if pd.isna(x) or str(x).strip() == "":
                return 0
            x_str = str(x).strip().lower()
            if x_str == 'true':
                return 1
            elif x_str == 'false':
                return 0
            elif any(char.isdigit() for char in x_str):
                return 1
            else:
                return 0

        self.df['Garden'] = self.df['Garden'].apply(helper).astype("Int64")
        self.df['Terrace'] = self.df['Terrace'].apply(helper).astype("Int64")

    # Clean numeric columns and ensure integers
    def clean_numeric_columns(self, columns):
        for col in columns:
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce').astype("Int64")

    # Clean surface columns (remove "m²", keep as float)
    def clean_surface_columns(self, columns):
        for col in columns:
            self.df[col] = self.df[col].astype(str).str.replace(r'[^\d.]', '', regex=True)
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce')

     # Clean state of building  0 , 1, 2       
    def clean_state_of_building(self, x):
        if pd.isna(x) or str(x).strip() == "":
            return pd.NA
        x = str(x).strip().lower()
        if any(word in x for word in ["to renovate", "to be renovated", "to restore"]):
            return 0
        elif "normal" in x:
            return 1
        elif any(word in x for word in ["excellent", "new", "fully renovated"]):
            return 2
        else:
            return pd.NA

    def clean_state_of_building_column(self):
        if 'State of building' in self.df.columns:
            self.df['State of building'] = self.df['State of building'] \
                .apply(self.clean_state_of_building).astype("Int64")

    # Clean Equipped kitchen column
    def clean_equipped_kitchen(self):
        def helper(x):
            if pd.isna(x) or str(x).strip() == "":
                return None
            try:
               return int(float(x))
            except:
                 return None

        self.df['Equipped kitchen'] = self.df['Equipped kitchen'].apply(helper).astype("Int64")
        return self.df     
    
     
    def clean_furnished(self):
        self.df["Furnished"] = self.df["Furnished"].apply(self.clean_boolean_column).astype("Int64")
        return self.df

    def clean_open_fire(self):
        self.df["Open fire"] = self.df["Open fire"].apply(self.clean_boolean_column).astype("Int64")
        return self.df

    def clean_swimming_pool(self):
        self.df["Swimming pool"] = self.df["Swimming pool"].apply(self.clean_boolean_column).astype("Int64")
        return self.df
    
    def clean_locality_name(self):
        def helper(x):
            if pd.isna(x) or str(x).strip() == "":
                return None
            x_str = html.unescape(str(x))
            x_str = re.sub(r'[^A-Za-z0-9\s\-]', '', x_str)
            x_str = ' '.join(x_str.split())
            return x_str if x_str else None
        self.df['Locality name'] = self.df['Locality name'].apply(helper).astype("string")
        return self.df
    def save_to_csv(self, file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        self.df.to_csv(file_path, index=False)
        return file_path
    

    # Apply all cleaning steps
    def clean_all(self):
        #self.clean_locality_name()
        self.clean_price()
        #self.clean_property_type()
        self.clean_garden_terrace()
        self.clean_numeric_columns(['Number of rooms', 'Number of facades', 'Living area'])
        self.clean_surface_columns(['Garden Surface', 'Terrace Surface'])
        self.clean_equipped_kitchen()
        self.clean_furnished()
        self.clean_open_fire()
        self.clean_swimming_pool()
        #self.clean_state_of_building_column()
        return self.df