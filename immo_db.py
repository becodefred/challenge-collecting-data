
import pandas as pd


col_names = [
    "Locality",
    "Type",
    "Subtype",
    "Price",
    "Sale",
    "Number_rooms",
    "Area",
    "Fully_equipped_kitchen",
    "Furnished",
    "Open_fire",
    "Terrace",
    "Ter_Area",
    "Garden",
    "Area_garden",
    "Livable_surface_area",
    "Surface_area_land",
    "Numb_facades",
    "Swimming_pool"
    "State"
]

immo_db = pd.DataFrame(columns = col_names)


immo_db = immo_db.append({    
    "Locality" : "Liège",
    "Type" : "Flat",
    "Subtype" : None,
    "Price" : 200.000,
    "Sale" : "",
    "Number_rooms" : "",
    "Area" : "",
    "Fully_equipped_kitchen" : "",
    "Furnished" : "",
    "Open_fire" : "",
    "Terrace" : "",
    "Ter_Area" : "",
    "Garden" : "",
    "Area_garden" : "",
    "Livable_surface_area" : "",
    "Surface_area_land" : "",
    "Numb_facades" : "",
    "Swimming_pool" : "",
    "State" : ""}, ignore_index=True)
print(immo_db)


immo_db.to_csv(r'C:\Users\Guillaume\Desktop\Stage\Mémoire\Python\Crunchbase_v5\tweet_v3_2.xlsx', index=False)

