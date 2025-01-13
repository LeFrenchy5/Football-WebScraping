# Football-WebScraping

Directory Contains:

Player_id - Contains a csv file called Team_links.csv which contains all the links for the teams on FBREF

Fbref Folder - Contains team folders for the teams selected by the user, each of these team folders contain multiple csv for each table on FBREF

understat Folder - Contains a csv for the teams selected by the user, the csv files contains the teams shots from understat

Fbref.py - This contains the functions used by main to webscrape the data from FBEF and clean each csv file to be used for analysis

understat.py - This contains the functions used by main to webscrape the data from understat for the selected team

main.py - The main.py contains the code for the user to select a team, then using both Fbref.py and understat.py to webscrape the data

**Skills Used: Python - pandas, numpy, tkinter, requests, BeautifulSoup, StringIO, os, shutil, ipywidgets, json**
