
import pandas as pd
from immo_db import *
from link_pages import explore_page

import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

immo_db = create_db()

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path = r"C:\Users\Guillaume\Geckodriver\geckodriver.exe")

for p in range(1):
    
    p += 1
    
    if p == 1:
        
        url = "https://www.immoweb.be/fr/recherche/maison-et-appartement/a-vendre?countries=BE"
        immo_db = explore_page(url, immo_db, driver)
        
    else:
        
        url = "https://www.immoweb.be/fr/recherche/maison-et-appartement/a-vendre?countries=BE&page={}&orderBy=relevance".format(p)
        immo_db = explore_page(url, immo_db, driver)


print(immo_db)
#immo_db.to_csv(r"C:\Users\Guillaume\git\challenge-collecting-data\test.csv", index=False)


    





