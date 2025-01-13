import requests
from io import StringIO
from  bs4 import BeautifulSoup
import pandas as pd
import os
import shutil
import ipywidgets as widgets
from IPython.display import display


"""
A function to request the players links for the selected team.
Parameters:
- url (str): The url of the team's page on Fbref

Returns:
- player_info (dataframe): A dataframe containing players name, position and link
"""
def get_player_links(url):
    # Send a get request to th url
    data = requests.get(url)

    # Getting links for each player
    soup = BeautifulSoup(data.text, 'html.parser')
    # Find the first stats table and extract all 'a' tags
    players = soup.select('table.stats_table')[0]
    links = players.find_all('a')
    links = [ l.get('href') for l in links]
    links = [l for l in links if '/players/' in l]

    # Taking every player link and removing the summary links
    links = [l for l in links if 'summary' not in l]

    # Creating a dataframe of the players information and links
    html_data = StringIO(data.text) # Change made
    player_stats = pd.read_html(html_data)[0]
    player_stats.columns = player_stats.columns.droplevel() 
    player_info = player_stats[['Player','Pos']][0:len(player_stats)-2]

    player_info['links'] = [l for l in links]
    player_info['id'] = player_info['links'].str.extract(r'players/([^/]+)/')

    return player_info

"""
A function that splits the goalkeepers and outfield players, and calls the appropriate function for each position.
Parameters:
- players (dataframe): A dataframe containing the players information from get_player_links 
- team_selected (str): The name of the team that was selected by the user
"""
def get_stats(players,team_selected):

    #checking if a folder exists for the team
    if not os.path.exists(f'fbref//{team_selected}'):
        os.makedirs(f'fbref//{team_selected}')
    else:
        shutil.rmtree(f'fbref//{team_selected}')
        os.makedirs(f'fbref//{team_selected}')

    
    # Iterating through the players list for the team 
    for index, player in players.iterrows():
        url = f"https://fbref.com{player['links']}" # Fetchs The players individual player page

        if player['Pos'] == 'GK':
            get_goalkeeper_stats(url,player,team_selected)
        else:
            get_player_stats(url,player,team_selected)

"""
A function that iterates through each table for a outfield player and saves the data to different csv files for each table
Paramters:
- url (str): The url of the players page
- player (series): A series containing the players information
- team_selected (str): The name of the selected team by the user
"""
def get_player_stats(url,player,team_selected):        
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise and exception for error HTTP status
        soup = BeautifulSoup(response.text, 'html.parser')

        for table_num,table_name in tables.items():
            if table_num == 11:
                table_id = titles[table_num]['id'] + str(player['id'])
                table = soup.find('table', {'id': table_id})
                
                if table:
                    html_data = StringIO(str(table)) # Change made
                    df = pd.read_html(html_data)[0]
                    df.columns = df.columns.droplevel()
                    df['Player'] = player['Player']
                    df['Position'] = player['Pos']

                    filename = f"fbref\\{team_selected}\\{team_selected}_{table_name}.csv"
                    if not os.path.isfile(filename):
                        df.to_csv(filename, index=False, encoding='utf-8')
                    else:
                        df.to_csv(filename, mode='a', header=False, index=False, encoding='utf-8')
                    print(f"Successfully Extracted {table_name} for {player['Player']}")
                else:
                    print(f"Table {table_name} not found for {player['Player']}")
            else:
                table_id = titles[table_num]['id']
                table = soup.find('table', {'id': table_id})

                if table:
                    html_data = StringIO(str(table)) # Change made
                    df = pd.read_html(html_data)[0]
                    df.columns = df.columns.droplevel()
                    df['Player'] = player['Player']
                    df['Position'] = player['Pos']

                    filename = f"fbref\\{team_selected}\\{team_selected}_{table_name}.csv"
                    if not os.path.isfile(filename):
                        df.to_csv(filename, index=False, encoding='utf-8')
                    else:
                        df.to_csv(filename, mode='a', header=False, index=False, encoding='utf-8')
                    print(f"Successfully Extracted {table_name} for {player['Player']}")
                else:
                    print(f"Table {table_name} not found for {player['Player']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {player['Player']} page: {e}")
    except Exception as e:
        print(f"Error processing {player['Player']} page: {e}")

"""
A function that iterates through each table for a goalkeeper and saves the data to different csv files for each table
Paramters:
- url (str): The url of the players page
- player (series): A series containing the players information
- team_selected (str): The name of the selected team by the user
"""
def get_goalkeeper_stats(url,player,team_selected):
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise and exception for error HTTP status
        soup = BeautifulSoup(response.text, 'html.parser')

        for table_num,table_name in Gk_tables.items():
            if table_num == 13:
                table_id = Gk_titles[table_num]['id'] + str(player['id'])
                table = soup.find('table', {'id': table_id})
                
                if table:
                    html_data = StringIO(str(table)) # Change made
                    df = pd.read_html(html_data)[0]
                    df.columns = df.columns.droplevel()
                    df['Player'] = player['Player']
                    df['Position'] = player['Pos']

                    filename = f"fbref\\{team_selected}\\{team_selected}_{table_name}.csv"
                    if not os.path.isfile(filename):
                        df.to_csv(filename, index=False, encoding='utf-8')
                    else:
                        df.to_csv(filename, mode='a', header=False, index=False, encoding='utf-8')
                    print(f"Successfully Extracted {table_name} for {player['Player']}")
                else:
                    print(f"Table {table_name} not found for {player['Player']}")
            else:
                table_id = Gk_titles[table_num]['id']
                table = soup.find('table', {'id': table_id})
                
                if table:
                    html_data = StringIO(str(table)) # Change made
                    df = pd.read_html(html_data)[0]
                    df.columns = df.columns.droplevel()
                    df['Player'] = player['Player']
                    df['Position'] = player['Pos']

                    filename = f"fbref\\{team_selected}\\{team_selected}_{table_name}.csv"
                    if not os.path.isfile(filename):
                        df.to_csv(filename, index=False)
                    else:
                        df.to_csv(filename, mode='a', header=False, index=False, encoding='utf-8')
                    print(f"Successfully Extracted {table_name} for {player['Player']}")
                else:
                    print(f"Table {table_name} not found for {player['Player']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {player['Player']} page: {e}")
    except Exception as e:
        print(f"Error processing {player['Player']} page: {e}")

"""
Defining table mappings and titles used to locate the correct tables in the HTML for Fbref
"""
tables = {
    1 : 'last_5_matches',
    2 : 'standard_stats',
    3 : 'shooting',
    4 : 'passing',
    5 : 'pass_types',
    6 : 'goals_shot_creation',
    7 : 'defensive_actions',
    8 : 'possesion',
    9 : 'playing_time',
    10 : 'miscellaneous_stats',
    11 : 'player_club_summary'
} 

Gk_tables = {
    1 : 'last_5_matches',
    2 : 'goalkeeping',
    3 : 'advanced_goalkeeping',
    4 : 'standard_stats',
    5 : 'shooting',
    6 : 'passing',
    7 : 'pass_types',
    8 : 'goals_shot_creation',
    9 : 'defensive_actions',
    10 : 'possesion',
    11: 'playing_time',
    12 : 'miscellaneous_stats',
    13 : 'player_club_summary'
}

titles = {
    1 : ({"id": "last_5_matchlogs"}),
    2 : {"id": "stats_standard_dom_lg"},
    3 : ({"id":"stats_shooting_dom_lg"}),
    4 : ({"id":"stats_passing_dom_lg"}),
    5 : ({"id":"stats_passing_types_dom_lg"}),
    6 : ({"id":"stats_gca_dom_lg"}),
    7 : ({"id":"stats_defense_dom_lg"}),
    8 : ({"id":"stats_possession_dom_lg"}),
    9 : ({"id":"stats_playing_time_dom_lg"}),
    10 : ({"id":"stats_misc_dom_lg"}),
    11 : ({"id":"stats_player_summary_"})
}

Gk_titles = {
    1 : ({"id": "last_5_matchlogs"}),
    2 : ({"id": "stats_keeper_dom_lg"}),
    3 : ({"id": "stats_keeper_adv_dom_lg"}),
    4 : {"id": "stats_standard_dom_lg"},
    5 : ({"id":"stats_shooting_dom_lg"}),
    6 : ({"id":"stats_passing_dom_lg"}),
    7 : ({"id":"stats_passing_types_dom_lg"}),
    8 : ({"id":"stats_gca_dom_lg"}),
    9 : ({"id":"stats_defense_dom_lg"}),
    10 : ({"id":"stats_possession_dom_lg"}),
    11 : ({"id":"stats_playing_time_dom_lg"}),
    12 : ({"id":"stats_misc_dom_lg"}),
    13 : ({"id":"stats_player_summary_"})
}

## Transforming and Cleaning The Csv files

"""
A function that separates different CSV files to be cleaned differently. 
Parameters: 
- team_selected (str): The name of the selected team.
"""
def cleaning(team_selected):
    # Iterate Through the folder to retrieve each file
    folder_path = f"fbref\\{team_selected}"
    #folder_path = f"D:/Learning/Portfolio/Web Scraping/Liverpool/fbref/"

    for file in os.listdir(folder_path):
        if file.endswith('.csv'):
            file_path = os.path.join(folder_path, file)

            if 'last_5_matches' in file_path:
                clean_last_5(file_path)
                print(f'Just Cleaned {file_path}')
            else:
                clean_csv(file_path)
                print(f'Just Cleaned {file_path}')

"""
A function that cleans all CSV files except the last 5 games.
Parameters:
- file_path (str): The path to the CSV file to be cleaned
"""
def clean_csv(file_path):
    df = pd.read_csv(file_path)
     
     # Drop The matches column
    df = df.drop(columns='Matches')

    # Filter rows where the season column matches desired format
    df = df.dropna(subset=['Season'])
    df = df[df['Season'].str.match(r'\d{4}-\d{4}')]

    df.to_csv(file_path, index= False, encoding='utf-8')

"""
A function that cleans the last 5 matches only.
Parameters:
- file_path (str): The path to the csv file to be cleaned
"""
def clean_last_5(file_path):
    df = pd.read_csv(file_path)

    # Drop The Match Report column
    df = df.drop(columns='Match Report')

    # Change Result to result (W,D,L) and score (3-3)
    df['Score'] = df['Result'].apply(lambda x: x.split()[1])
    df['Result'] = df['Result'].apply(lambda x: x.split()[0])

    df.to_csv(file_path, index=False, encoding='utf-8')