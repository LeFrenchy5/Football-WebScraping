import requests
from bs4 import BeautifulSoup
import json
import pandas as pd


def get_player_links(url):
    # Send a GET request to the URL
    data = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(data.text, 'html.parser')

    # Find the script tag containing player data
    script = soup.find('script', string=lambda string: string and 'var playersData' in string)

    # Extract JSON string
    json_text = script.string
    json_start= json_text.find("JSON.parse('") + len("JSON.parse('")
    json_end = json_text.rfind("')")
    json_data = json_text[json_start:json_end].encode('utf-8').decode('unicode_escape')

    players_data = json.loads(json_data)

    player = {}

    for x in players_data:
        player[x['player_name']] = x['id']

    return player


# Using requests and BeautifulSoup to get player shot data from understat.com using the player_id dataframe as a player index
def get_player_shots(player,team_selected):
    base_url = 'https://understat.com/player/'
    team_shots = pd.DataFrame() # Creating a dataframe to join all players shot together into a team shots dataframe

    for name, id in player.items():
        url = base_url + str(id)
        
        # Calling our url 
        res = requests.get(url)
        soup = BeautifulSoup(res.content,'lxml')
        scripts = soup.find_all('script')
        strings = scripts[3].string

        # Removing data thats not needed
        ind_start = strings.index( "('") + 2
        ind_end = strings.index("')")

        
        json_data = strings[ind_start:ind_end]
        json_data = json_data.encode('utf8').decode('unicode_escape')

        # Using the json library to convert from string to json format
        data = json.loads(json_data)
        
        # Normalize the data 
        df = pd.json_normalize(data)

        # Concat all player shots data into a team shots dataframe
        team_shots = pd.concat([team_shots,df], ignore_index=True)
        print(f"Successfully Saved {name} Shots Data")

    # Saving team dataframe to a csv
    team_shots.to_csv(f'understat//{team_selected}_shots.csv')
    print(f'Successfully Saved {team_selected} Shots Dataframe')