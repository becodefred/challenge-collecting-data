BeCode challenge : from 18/11/2020 to 23/11/2020 \
Name of the challenge : ImmoEliza \
Contributors : Guillaume, Reza, Frédéric \


#Collect data from immoweb

The code is divided in 4 files:

- main.py: this file needs to be run in order to extract the properties. We need to specify in this page:

  - the group of pages we want
  - the number of pages extracted at once
  - in the csv file, where we store everything
  
- immo_db.py: functions that create database and fill them with data

- link_values.py: the function's goal is to extract the following info from a page:

  - Number of rooms
  - If there is a equiped kitchen
  - If there is a terasse and its area
  - If there is a garden and its area
  - The livable area
  - If the property s furnished
  - If there is an open fire
  - The number of facades
  - If there is a pool
  - The state of the property
  
- link_pages.py: this function adds the data in the dataframe and extracts the rest of the data:

  - Its locality
  - Its postal code
  - Its price
  - If the property has already been built
  
We used immoweb to extract our data. We scraped 334 pages of selling properties and 7 pages of renting properties in order to reach more than 10.000 lines.


