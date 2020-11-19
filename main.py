
import pandas as pd
from immo_db import *
from link_pages import explore_page

immo_db = create_db()

for p in range(1):
    
    p += 1
    
    if p == 1:
        
        url = "https://www.immoweb.be/fr/recherche/maison-et-appartement/a-vendre?countries=BE"
        immo_db = explore_page(url, immo_db)
        
    else:
        
        url = "https://www.immoweb.be/fr/recherche/maison-et-appartement/a-vendre?countries=BE&page={}&orderBy=relevance".format(p)
        immo_db = explore_page(url, immo_db)


print(immo_db)
#immo_db.to_csv("", index=False)


