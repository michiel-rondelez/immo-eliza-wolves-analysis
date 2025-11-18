import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px
from deep_translator import GoogleTranslator

properties_data_og = pd.read_csv("clean_data_0.csv")
threshold = properties_data_og["Price"].quantile(0.90)
properties_data_og = properties_data_og[properties_data_og["Price"]<= threshold.astype(int)]

def map_per_type(type_property):
    properties_data = properties_data_og[properties_data_og["Type of property"] == type_property].copy()
    #calculate and store median price per postal code###########################################################
    price_per_code = properties_data.groupby("Postal code")["Price"].median().reset_index().rename(columns={"Price":"median_price"})

    #load geographical data and get English names to save the Peace#########################################################################
    gdf_pc = gpd.read_file("data/postal-codes-belgium.geojson")

    #get unique names
    def select_primary_name(row):
        lang_combo = row["official_language_or_language_combination"]
        if pd.isna(lang_combo):
            return None

        # Split e.g. "FR-nl" -> ["FR", "nl"]
        parts = str(lang_combo).split("-")

        # Primary language = the one in ALL CAPS (if any)
        primary = None
        for p in parts:
            if p == p.upper():
                primary = p
                break
        if primary is None:
            primary = parts[0].upper()  # fallback

        col_map = {
            "FR": "municipality_name_french",
            "NL": "municipality_name_dutch",
            "DE": "municipality_name_german",
        }
        col = col_map.get(primary)
        if col is None:
            return None

        return row[col]

    gdf_pc["municipality_local"] = gdf_pc.apply(select_primary_name, axis=1)

    unique_local = sorted(
        {n for n in gdf_pc["municipality_local"].dropna()
        if isinstance(n, str) and n.strip() != ""}
    )

    #translate
    translator = GoogleTranslator(source="auto", target="en")
    name_to_en = {}
    for name in unique_local:
        try:
            en = translator.translate(name)
        except Exception as e:
            print(f"Translation failed for '{name}': {e}")
            en = name  # fallback: keep original
        name_to_en[name] = en

    #store en name in the geo db
    gdf_pc["municipality_english"] = gdf_pc["municipality_local"].map(name_to_en)


    #Merge geographical data with postal codes############################################################
    gdf_pc["Postal Code"] = price_per_code["Postal code"].astype(int)

    gdf_merged = gdf_pc.merge(
        price_per_code, 
        left_on="post_code", 
        right_on="Postal code", 
        how="left")

    #Plot the map#############################################################
    geojson_data = gdf_merged.__geo_interface__

    fig = px.choropleth_mapbox(
        gdf_merged,
        geojson=geojson_data,
        locations="post_code",
        featureidkey="properties.post_code",
        color="median_price",
        hover_name="municipality_english",
        hover_data={"post_code": True,"median_price": ":,.0f",},
        color_continuous_scale="Viridis",
        mapbox_style="open-street-map",
        zoom=7,
        center={"lat":50.5039, "lon": 4.4699},
        opacity=0.7,
        labels={"median_price":F"Median {type_property} price (€)"}
    )

    fig.update_layout(margin={"r":0, "t":30, "l":0, "b":0}, title=F"Median {type_property} Price by Postal Code")

    fig.show()

map_per_type("House")
#map_per_type("Appartment")