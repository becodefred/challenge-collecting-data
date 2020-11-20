import selenium
import re

from link_values import get_info_prop
from immo_db import add_value

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

#url='https://www.immoweb.be/fr/recherche/maison-et-appartement/a-vendre?countries=BE'


def explore_page(url, df):
    
    

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path = r"C:\Users\Guillaume\Geckodriver\geckodriver.exe")
    
    #Going to the webpage
    driver.get(url)
    
    #Scraping data from the following class
    ty = driver.find_elements_by_class_name("card__title-link")
    
    loc = driver.find_elements_by_class_name("card--results__information--locality")
    
    links = [elem.get_attribute('href') for elem in ty]
    
    pi = []
    for i in ty:
        
        pi.append(i.text)
        
    
    pu = []
    for j in loc:
        
        pu.append(j.text)
    
    driver.close()
    
    for y in range(len(links)):
        
       info = get_info_prop(links[y])
       
           
       x = re.search("[0-9]{4} ", pu[y])
        
       if x:
            
           locality = pu[y].split(" ")[1]
       
       for k in range(14):
            
           print(locality, pi[y], info[k])
           
       df = add_value(df, locality, pi[y], info[0], info[1], info[2],
                  info[3], info[4], info[5], info[6], info[7], info[8],
                  info[9], info[10], info[11], info[12], info[13])
       
    
    return df
       




