#BeCode challenge : from 18/11/2020 to 23/11/2020
#Name of the challenge : ImmoEliza
#Contributors : Guillaume, Reza, Frédéric

import pandas as pd
import re
import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options



def joiner_num(li): 
    
    '''
    function that joins all terms in a list without space
    Requires a list to work 
    Will be used to gather numbers back together after using regEx
    '''
    
    if len(li) > 1:
        li = [''.join(li)]
        
        
    return li


def joiner_word(lo): 
    
    '''
    function that join all terms in a list with a space in between each
    Requires a list to work
    Will be used to isolate a word after using regEx
    '''
    
    if len(lo) > 1:
        lo = [' '.join(lo)]
        
        
    return lo

def get_info_prop(url, driver):
    
    
    '''
    Function that takes an url to work and a driver:
        - this url of the page will use
        - the driver needed to access the pages with selenium
    
    When the page has been scraped, it returns the needed values 
    in order to store them later in a pandas dataframe.
    
    '''
    
    
    
    
    #Setting up variables and give them default values
    room = None
    terrasse = 0
    sur_terrasse = None
    kitchen = 0
    jardin = 0
    sur_jardin = None
    sur_habi = None
    sur_ter = None
    furnished = 0
    open_fire = 0
    fa = None
    piscine = 0
    state = None
    
    
    #Going to the webpage
    driver.get(url)
    
    #Scraping data from the following class
    elem = driver.find_elements_by_class_name("accordion--section")
    
    #loop to run all the blocks of information identified in immoweb
    for u in elem:
        
        #Condition to check if the block has info in it
        NoneType = type(None)
        if type(u) != NoneType:
            
            
            #Spliting all pieces of information
            spt = u.text.split("\n")
            
            #Going through all data to identify their role
            for i in spt:
            
                
                #Finding the number of rooms and not their surface
                #We call joiner_num in order to gather the numbers found using Regex
                #Once the numbers are one, we extract it from the list
                if "Chambres" in i and "Surface" not in i:
                    
                    room = re.findall("\d",i)
                    room = joiner_num(room)[0]
                
                #Finding if the kitchen is equiped or not 
                # 1: Yes and 0: No
                if "cuisine" in i and "équipée" in i and "pas" not in i:
                    kitchen = 1
                
                
                #Finding if a terasse is present and its area
                #if not terasse keeps its default value of 0
                if "terrasse" in i and "Surface" in i:
                    
                    terrasse = 1
                    sur_terrasse = re.findall("\d",i)
                    sur_terrasse = joiner_num(sur_terrasse)[0]
                    
                    
                #Finding if a garden is present and its area 
                #if not garden keeps its default value of 0
                if "jardin" in i and "Surface" in i:
                    
                    jardin = 1
                    sur_jardin = re.findall("\d",i)
                    sur_jardin = joiner_num(sur_jardin)[0]
                
                #Finding the living area
                if "Surface habitable" in i:
                    
                    sur_habi = re.findall("\d",i)
                    sur_habi = joiner_num(sur_habi)[0]
                    
                #Finding out the total land area
                if "Surface du terrain" in i:
                    
                    sur_ter = re.findall("\d",i)
                    sur_ter = joiner_num(sur_ter)[0]
                
                
                #Finding out if the property is furnished 
                if "Meublé" in i and "pas" not in i:
                    
                    furnished = 1
                
                #Finding out if there is an open fire
                
                if "Feu ouvert" in i:
                    
                    open_fire = 1
                    
                #Finding the number of facades
                if "Façades" in i:
                    
                    fa = re.findall("\d",i)
                    fa = joiner_num(fa)[0]
                 
                #Finding if there is a pool
                if "piscine" in i or "Piscine" in i:
                    
                    piscine = 1
                
                #Finding the state of the house
                #We extract the value after "Etat du bâtiment"
                if "État" in i:
                    
                    et = i.split()
                    state = et[3:]
                    state = joiner_word(state)[0]
      
    
    
    
    #returning all the variables to store them in our pandas dataframe
    return (room, kitchen, terrasse, 
            sur_terrasse, jardin, sur_jardin, sur_habi, sur_ter, furnished, 
            open_fire, fa, piscine, state)
          
        





