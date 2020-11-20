
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def create_db():
    
    #Creating columns names for our dataframe 
    col_names = [
        "Locality",
        "Type",
        "Price",
        "Number_rooms",
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
        "Swimming_pool",
        "State"
    ]
    
    #Generating the dataframe with our columns
    x = pd.DataFrame(columns = col_names)
    
    return x

immo_db = create_db()


def add_value(df, locality, typ, price, room, kitchen, terrasse, sur_terrasse, 
              jardin, sur_jardin, sur_habi, sur_ter, furnished, open_fire, 
              fa, piscine, state):
    

    #Adding a new value to the dataframe
    df = df.append({    
        "Locality" : locality,
        "Type" : typ,
        "Price" : price,
        "Number_rooms" : room,
        "Fully_equipped_kitchen" : kitchen,
        "Furnished" : furnished,
        "Open_fire" : open_fire,
        "Terrace" : terrasse,
        "Ter_Area" : sur_terrasse,
        "Garden" : jardin,
        "Area_garden" : sur_jardin,
        "Livable_surface_area" : sur_habi,
        "Surface_area_land" : sur_ter,
        "Numb_facades" : fa,
        "Swimming_pool" : piscine,
        "State" : state}, ignore_index=True)

    return df


