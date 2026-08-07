import numpy as np
import pandas as pd

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats, playercompare

filepath = r"NBA\stats\AE_FullStats.json"

nameType = 1

prompt = "Input the first player's full name (first and last): "

while True:
    name = input(prompt).strip()
    separator_count = name.count(" ") + name.count("-")

    if not (1 <= separator_count <= 2):
        prompt = "Try Again: "
        continue

    try:
        player_id = players.find_players_by_full_name(name)[0]["id"]
        break
    except (NameError, IndexError):
        prompt = "Player not found. Try Again: "

name = players.find_player_by_id(player_id)['full_name']

#ensures the initials are correct for the player name inputted
if separator_count == 1:
    initials = name[0].capitalize() + name[name.find(" ") + 1].capitalize() 
elif separator_count == 2:
     initials = name[0].capitalize() + name[name.find(" ") + 1].capitalize() + name[-name.find(" ") - 1].capitalize()

print(name)
print(initials)

seasonStats1 = playercareerstats.PlayerCareerStats(id).get_data_frames()[1]

with open (filepath, 'w') as stats1:
    stats1.write(seasonStats1.to_json(orient='records', lines=True))