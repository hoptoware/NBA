import numpy as np
import pandas as pd

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats, playercompare

filepath = r"NBA\stats\AE_FullStats.json"


name1 = input("Input the first player's full name (first and last): ")
if name1.count(" ") + name1.count("-") == 0:
    name1 = input("Try Again: ")
    while name1.count(" ") + name1.count("-") == 0:
        name1 = input("Try Again: ")
elif name1.count(" ") + name1.count("-") == 1:
    initials1 = name1[0].capitalize() + name1[name1.find(" ") + 1].capitalize()
elif name1.count(" ") + name1.count("-") == 2:
    initials1 = name1[0].capitalize() + name1[name1.find(" ") + 1].capitalize() + name1[-name1.find(" ") - 1].capitalize()
else:
    name1 = input("Try Again: ")
    while name1.count(" ") + name1.count("-") == 0:
        name1 = input("Try Again: ")
#print(initials)

while True:
    try:
        id1 = players.find_players_by_full_name(name1)[0]['id']
        break
    except NameError:
        name1 = input("Try Again: ")

name1 = players.find_player_by_id(id1)['full_name']
print(name1)

seasonStats1 = playercareerstats.PlayerCareerStats(id1).get_data_frames()[1]

with open (filepath, 'w') as stats1:
    stats1.write(seasonStats1.to_json(orient='records', lines=True))
