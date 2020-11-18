
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def create_db():
    
    #Creating columns names for our dataframe 
    col_names = [
        "Locality",
        "Type",
        "Subtype",
        "Price",
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
    
    #Generating the dataframe with our columns
    x = pd.DataFrame(columns = col_names)
    
    return x

immo_db = create_db()



#Adding a new value to the dataframe
immo_db = immo_db.append({    
    "Locality" : "Liège",
    "Type" : "Flat",
    "Subtype" : None,
    "Price" : 200.000,
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


#exporting the dataframe to a csv file
immo_db.to_csv("", index=False)

