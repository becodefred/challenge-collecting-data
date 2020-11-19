import selenium

from link_values import get_info_prop
from immo_db import add_value

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#url='https://www.immoweb.be/fr/recherche/maison-et-appartement/a-vendre?countries=BE'


def explore_page(url, df):
        
    driver = webdriver.Firefox(executable_path = r"C:\Users\Guillaume\Geckodriver\geckodriver.exe")
    
    #Going to the webpage
    driver.get(url)
    
    #Scraping data from the following class
    elems = driver.find_elements_by_class_name("card__title-link")
    
    links = [elem.get_attribute('href') for elem in elems]
    
    pi = []
    for i in elems:
        
        pi.append(i.text)
        
    
    driver.close()
    
    for y in range(len(links)):
        
       info = get_info_prop(links[y], pi[y])
       
       for k in range(15):
           
           print(info[k])
           
       df = add_value(df, info[0], info[1], info[2], info[3], info[4],
                  info[5], info[6], info[7], info[8], info[9], info[10],
                  info[11], info[12], info[13], info[14], info[15])
       
    
    return df
       










