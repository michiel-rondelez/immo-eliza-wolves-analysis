🏠 Immo Eliza – Data Cleaning & Analysis
--------------------------------------------------------------------------------------

This project focuses on cleaning, analyzing, and exploring a real dataset from the Belgian real estate market. The work was done in a group and follows a classic data analysis workflow: cleaning, normalization, visual exploration, and preparing the dataset for modeling.

![Data Analysis](https://images.pexels.com/photos/3184292/pexels-photo-3184292.jpeg)




📌 Main Objectives of the Project
--------------------------------------------------------------------------------------

* Understand the structure of the dataset and detect common issues (missing values, incorrect formats, duplicates, outliers…).

* Perform a complete cleaning of the dataset using a clear and reproducible logic.

* Normalize variables and standardize formats to analyze them without errors.

* Conduct exploratory analysis using visualizations and basic statistics.


📁 Project Structure
--------------------------------------------------------------------------------------

.

├── data/

│   ├── raw/

│   │   └── data.csv           # Original dataset

│   └── clean_data.csv         # Cleaned dataset generated

│

├── data_cleaning.py           # Main cleaning script

├── data_cleaner_class.py      # Class containing cleaning functions

│

├── visuals/                   # Generated plots and visuals

├── screenshots/               # Images used for documentation

│

├── visualizing.py             # Graphs and analysis

│

├── README.md                  # This file

└── .gitignore




🧹 What the script does
--------------------------------------------------------------------------------------

The file data_cleaning.py carries out several important steps:

✔ General Cleaning

* Removal of duplicates based on Property ID.

* Removal of properties without a valid price.

* Exclusion of unwanted sale types (Rent, PublicSale, Share).

✔ Format Fixes

* Convert strange HTML text in the Locality name column.

* Convert numerical columns to the correct format.

* Fill missing values with Unknown or 0.

* Remove unnecessary whitespace.

✔ Final Output

* The script generates a clean CSV file.



🛠️ Usage
--------------------------------------------------------------------------------------

* Clone the repository to your machine.

* Make sure you have Python 3.10+ installed.

* Install the required libraries



🧩 Small example (extract from the script)
--------------------------------------------------------------------------------------


    properties_data['Locality name'] = properties_data['Locality name'].apply(html.unescape)

    properties_data['Price'].replace(r'^\s*$|^0.00$', np.nan, regex=True)
    properties_data.dropna(subset=['Price'], inplace=True)
    properties_data = properties_data[properties_data['Price'] != 0]

    discarded = ['Rent', 'PublicSale', 'Share']
    properties_data = properties_data[~properties_data['Type of sale'].isin(discarded)]




📊 Exploratory Data Analysis
--------------------------------------------------------------------------------------

After cleaning the dataset, we performed a general exploratory analysis to better understand the variables and their relationships.

This included:

* Distribution visualizations

* Outlier detection

* Missing value analysis

* Comparison between property types

* Correlation calculation for all numerical variables

* A general heatmap to identify the strongest relationships

* All the analysis was done using Seaborn and Matplotlib.



⏱️ Timeline
--------------------------------------------------------------------------------------

This project was developed over several sessions during the bootcamp, combining data cleaning, exploration, and visualization.



🏛️ Personal Situation
--------------------------------------------------------------------------------------

This project is part of immoeliza_data_analysis, completed during the AI Bootcamp at BeCode as a practical exercise in cleaning and analyzing real-world datasets.