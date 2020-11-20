import selenium
import re

from link_values import get_info_prop
from immo_db import add_value

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


def explore_page(url, df, driver):
    
    

    
    #Going to the webpage
    driver.get(url)
    
    #Scraping data from the following class
    ty = driver.find_elements_by_class_name("card__title-link")
    
    loc = driver.find_elements_by_class_name("card--results__information--locality")
    
    price = driver.find_elements_by_class_name("card--result__price")
    
    links = [elem.get_attribute('href') for elem in ty]
    
    pi = []
    for i in ty:
        
        pi.append(i.text)
        
    
    pu = []
    for j in loc:
        
        pu.append(j.text)
    
    bi = []
    for x in price:
    
        bi.append(x.text)
        
    
    
    for y in range(len(links)):
        
       info = get_info_prop(links[y], driver)
       
           
       x = re.search("[0-9]{4} ", pu[y])
        
       if x:
            
           locality = pu[y].split(" ")[1]
           postal_code = pu[y].split(" ")[0]
           
       bi[y] = bi[y].split("\n")[1] 
       
       if "De" in bi[y]:
           
           build = 0
           
       else:
           
           build = 1
       
       for k in range(13):
            
           print(locality, postal_code, pi[y], bi[y], build, info[k])
           
       df = add_value(df, locality, postal_code, pi[y], build, bi[y], info[0], info[1],
                  info[2], info[3], info[4], info[5], info[6], info[7],
                  info[8], info[9], info[10], info[11], info[12])
       
    
    return df
       




