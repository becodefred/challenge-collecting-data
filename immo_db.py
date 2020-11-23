#BeCode challenge : from 18/11/2020 to 23/11/2020
#Name of the challenge : ImmoEliza
#Contributors : Guillaume, Reza, Frédéric

import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def create_db():
    
    '''
    Function built to create an empty dataframe with 
    the following column names
    '''
    
    #Creating columns names for our dataframe 
    col_names = [
        "Locality",
        "Postal code",
        "Type",
        "Build",
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


def add_value(df, locality, postal_code, typ, build, price, room, kitchen, terrasse, sur_terrasse, 
              jardin, sur_jardin, sur_habi, sur_ter, furnished, open_fire, 
              fa, piscine, state):
    
    '''
    Function that adds a row of information to the dataframe
    IT takes as arguments all the data gathered while scraping 
    
    '''
    #Adding a new value to the dataframe
    df = df.append({    
        "Locality" : locality,
        "Postal code" : postal_code,
        "Type" : typ,
        "Build" : build,
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


