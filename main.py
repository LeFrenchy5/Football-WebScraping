import Fbref as f
import understat as u

from tkinter import *
from tkinter import ttk
import pandas as pd

# Initialize the main application window To Select your specific team
root = Tk()
root.title('Pick A Team')
root.geometry('300x200')

# Read data from csv file containing team links
df = pd.read_csv('Player_id\Team_links.csv')

# Create a list of all unique leagues available in the dataset
league_options = [x for x in df['League'].unique()]

"""
A function to update the teams options based on the selected league
"""
def pick_team(event):
    combo1.config(value= [x for x in df[df['League'] == combo.get()]['Team']])

"""
A function to get the link of the selected team, as well as the team name
global variables:
- team_selected (str): The name of the team selected
- fbref_link (str): The link to the team selected for Fbref.com
- understat_link (str): The link to the team selected for understat.com
"""
def team_link(event):
    global fbref_link, understat_link, team_selected
    team_selected = combo1.get()
    fbref_link = df[df['Team'] == team_selected]['Link'].values[0]
    understat_link = f'https://understat.com/team/{team_selected}'

"""
A function to enable the Done button once a team is selected
"""
def enable_done_button(event):
    if combo1.get() is not None:
        done_button.config(state='normal')

"""
A function that combines fetching the team link and enabling the button.
This will be used on the bind
"""
def combined_handler(event):
    team_link(event)
    enable_done_button(event)

# Create a dropdown combobox for selecting a league
combo = ttk.Combobox(root, value = league_options)
combo.current(0) # Set the default selected league to the first option (Premier League)
combo.pack(pady=20) # Add padding around the combobox

# Bind the combobox to call the pick_team function when a league is selected
combo.bind('<<ComboboxSelected>>', pick_team)

# Create a dropdown combobox for selecting a team within the chosen league
combo1 = ttk.Combobox(root, value =['Select a League'])
combo1.current(0) # Set the default option
combo1.pack(pady=20) # Add padding around the combobox

# Bind the team combobox to call the combined_handler function when a team is selected
combo1.bind('<<ComboboxSelected>>', combined_handler)

# Create a 'Done' button to close the window, initially disabled until a team is selected
done_button = ttk.Button(text='Done', command=root.destroy, state='disabled')
done_button.pack(pady=20)

# Start the main event loop of the application
root.mainloop()

# Using the function from Fbref to get the players information for the selected team
fbref_players = f.get_player_links(fbref_link)

# Using a function from Fbref to get all the player stats tables for each player in the team
f.get_stats(fbref_players,team_selected)

# Finally we use a function from Fbref to do a basic clean of the data from the csv files
f.cleaning(team_selected)

# Using a function from understat file to get the players links
understat_player = u.get_player_links(understat_link)

# Using a funciton from the understat file to get all the players shots and save into one team csv
u.get_player_shots(understat_player, team_selected)
