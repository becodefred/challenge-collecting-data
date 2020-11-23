#BeCode challenge : from 18/11/2020 to 23/11/2020
#Name of the challenge : ImmoEliza
#Contributors : Guillaume, Reza, Frédéric

import selenium
import re
	
import time

from link_values import get_info_prop
from immo_db import add_value

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException


def explore_page(url, df, driver):
    
    '''
    This function goes through a page with 30 properties in it, 
    extract a few information (Locality, price, postal code, type) 
    as well as the link for each of those properties listed in the initial page.
    
    It also adds the values gathered in this function or in get_info_prop 
    to the database.
    
    It takes these arguments: 
        - the url of the initial page -> url
        - the database -> df
        - the driver -> driver
    '''

    try:
        #Going to the webpage
        driver.get(url)
        
        #Scraping data from the following class
        
        #get a list of types for all the properties
        ty = driver.find_elements_by_class_name("card__title-link")
        
        pi = []
        for i in ty:
            
            pi.append(i.text)
            
        #get a list of locality for all the properties
        loc = driver.find_elements_by_class_name("card--results__information--locality")
        
        pu = []
        for j in loc:
            
            pu.append(j.text)
        
        #get a list of prices for all the properties
        price = driver.find_elements_by_class_name("card--result__price")
                
        bi = []
        for x in price:
        
            bi.append(x.text)
        
        #Extract the links calling only the href from ty
        links = [elem.get_attribute('href') for elem in ty]
        
    
            
        #For how many links we have in the list, we extract the rest of 
        #the variables needed from the personnal page of the property
        for y in range(len(links)):
            
            
           info = get_info_prop(links[y], driver)
           
           
           #from the infos, seperating the postal code and the locality     
           x = re.search("[0-9]{4} ", pu[y])
            
           if x:
                
               locality = pu[y].split(" ")[1]
               postal_code = pu[y].split(" ")[0]
           
            #taking the right price 
           bi[y] = bi[y].split("\n")[1] 
           
           #If the price is an interval, that means the property is not finished yet
           #The presence of "De" in the price will give the info 
           if "De" in bi[y]:
               
               #Meaning it has not been built yet
               build = 0
               
           else:
               
               #the property is operational
               build = 1
           
            #Adding a print to see where we are at in the console
           for k in range(13):
                
               print(locality, postal_code, pi[y], bi[y], build, info[k])
           
            #Adding the values found in this function and in get_info_prop
           df = add_value(df, locality, postal_code, pi[y], build, bi[y], info[0], info[1],
                      info[2], info[3], info[4], info[5], info[6], info[7],
                      info[8], info[9], info[10], info[11], info[12])
           
    except TimeoutException:
            
        driver.close()


    #Returning the databse
    return df
       




