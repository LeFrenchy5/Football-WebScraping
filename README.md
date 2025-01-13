# Football-WebScraping

This repository contains scripts for web scraping football data from FBREF and Understat. The data collected is structured and stored in CSV files for further analysis.

## Project Motivation:

The project was undertaken to streamline the process of gathering football data from FBREF and Understat (For the top European Leagues), enabling more efficient data-driven decision making in football analysis.

## Directory Contains:

Player_id - Contains a csv file called `Team_links.csv` which contains all the links for the teams on FBREF

Fbref Folder - Contains team folders for the teams selected by the user, each of these team folders contain multiple csv for each table on FBREF

understat Folder - Contains a csv for the teams selected by the user, the csv files contains the teams shots from understat

Fbref.py - This contains the functions used by `main.py` to webscrape the data from FBEF and clean each csv file to be used for analysis

understat.py - This contains the functions used by `main.py` to webscrape the data from understat for the selected team

main.py - Contains the code for the user to select a team, then using both `Fbref.py` and `understat.py` to webscrape the data

requirements.txt - Contains the dependencies required to run the project

**Skills Used: Python - pandas, numpy, tkinter, requests, BeautifulSoup, StringIO, os, shutil, ipywidgets, json**

# How to Use:

1. **Clone the repository:** 
```
git clone https://github.com/LeFrenchy5/Football-WebScraping.git
```
2. **Install dependencies:** Ensure you have the required libraries installed (eg. requests, beautifulsoup, pandas
```
pip install -r requirments.txt
```
3.**Run the main script:** Execute `main.py` to start web scraping process
```
python main.py
```

## Software & Dependencies Used:
+ Python (Software)
+ Requests
+ Pandas
+ Numpy
+ tkinter
+ os
+ shutil
+ ipywidgets
+ json

## Data Sources:
+ **FBREF:** A comprehensive source for football statistics and history ( https://fbref.com/en/comps/9/Premier-League-Stats)
+ **Understat:** A website dedicated to advanced football statistics (https://understat.com)

## Data Pipeline:
1. **Web Scraping:** Data is scraped from FBREF and Understat using custom python functions (User Selected teams)
2. **Data Cleaning:** The scraped data from FBREF is cleaned then structured into csv files for further analysis, understat is structured straight into csv files
3. **Storage:** The cleaned data is stored into respective folders for each team

## Examples of Analysis:
+ Analysis of team or individual performances over current or past seasons
+ Comparison of player statistics across teams
+ Visualization of teams shot map per season

## Future Work:
+ Incorporate advanced analytics and visualizations for user selected teams
+ Automate the update process to keep data up to date
+ Extend the project to include more leagues and teams
+ Extend the project to include more statistics 

## Improvements:
+ Fix issue with individual "Player club summary" table on FBREF
+ Make table mappings more efficient
+ Utilize tkinter & windows to make the project more user friendly

## Portfolio Link:
- https://gavlestrangebusine.wixsite.com/data-analyst-portfol
