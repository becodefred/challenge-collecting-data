
import pandas as pd
import re
import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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

def get_info_prop(url, prop):
    
    
    '''
    Function that takes an url to work: this url will be used 
    to access the page using selenium.
    When the page has been scraped, it isolates needed values 
    in order to store them later in a pandas dataframe.
    
    '''
    
    
    
    
    #Setting up variables and give them default values
    locality = None
    type_prop = prop
    price = None
    room = None
    terasse = 0
    sur_terasse = None
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
    

    #setting up the driver
    driver = webdriver.Firefox(executable_path = r"C:\Users\Guillaume\Geckodriver\geckodriver.exe")
    
    #Going to the webpage
    driver.get(url)
    
    #Scraping data from the following class
    elem = driver.find_elements_by_class_name("accordion--section")
    
    #3 main blocks of information are identified
    for u in elem:
        
        #Spliting all pieces of information
        spt = u.text.split("\n")
        
        #Going through all data to identify their role
        for i in spt:
        
            #Used to extract the locality from the website
            x = re.search("[0-9]{4} - ", i)
            if x:
                
                i = i.split("- ")
                locality = i[1]
            
            #Finding the price and recompose it using joiner_num
            if "Prix" in i:
                
                price = re.findall("\d",i)
                price = joiner_num(price)
            
            #Finding the number of rooms and not their surface
            if "Chambres" in i and "Surface" not in i:
                
                room = re.findall("\d",i)
                room = joiner_num(room)
            
            #Finding if the kitchen is equiped or not 
            # 1: Yes and 0: No
            if "cuisine" in i and "équipée" in i and "pas" not in i:
                kitchen = 1
            
            
            #Finding if a terasse is present and its area
            #if not terasse keeps its default value of 0
            if "terasse" in i and "Surface" in i:
                
                terasse = 1
                sur_terasse = re.findall("\d",i)
                sur_terasse = joiner_num(sur_terasse)
                
                
            #Finding if a garden is present and its area 
            #if not garden keeps its default value of 0
            if "jardin" in i and "Surface" in i:
                
                jardin = 1
                sur_jardin = re.findall("\d",i)
                sur_jardin = joiner_num(sur_jardin)
            
            #Finding the living area
            if "Surface habitable" in i:
                
                sur_habi = re.findall("\d",i)
                sur_habi = joiner_num(sur_habi)
                
            #Finding out the total land area
            if "Surface du terrain" in i:
                
                sur_ter = re.findall("\d",i)
                sur_ter = joiner_num(sur_ter)
            
            
            #Finding out if the property is furnished 
            if "meublé" in i and "pas" not in i:
                
                furnished = 1
            
            #Finding out if there is an open fire
            
            if "Feu ouvert" in i:
                
                open_fire = 1
                
            #Finding the number of facades
            if "Façades" in i:
                
                fa = re.findall("\d",i)
                fa = joiner_num(fa)
             
            #Finding if there is a pool
            if "piscine" in i or "Piscine" in i:
                
                piscine = 1
            
            #Finding the state of the house
            if "État" in i:
                
                et = i.split()
                state = et[3:]
                state = joiner_word(state)
      
    
    driver.close()
    
    #returning all the variables to store them in our pandas dataframe
    return (locality, type_prop, price, room, kitchen, terasse, 
            sur_terasse, jardin, sur_jardin, sur_habi, sur_ter, furnished, 
            open_fire, fa, piscine, state)
          
        





