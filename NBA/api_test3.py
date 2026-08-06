import numpy as np
import pandas as pd

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats, playercompare

filepath = r"NBA\stats\AE_FullStats.json"

while True:
    name1 = input("Input the first player's full name (first and last): ").strip()

    if not name1 or (" " not in name1 and "-" not in name1):
        print("Try again. Include at least one space or hyphen.")
        continue

    try:
        id1 = players.find_players_by_full_name(name1)[0]["id"]
        break
    except (IndexError, KeyError):
        print("No player found. Try again.")

name1 = players.find_player_by_id(id1)["full_name"]
print(name1)

seasonStats1 = playercareerstats.PlayerCareerStats(id1).get_data_frames()[1]

with open (filepath, 'w') as stats1:
    stats1.write(seasonStats1.to_json(orient='records', lines=True))
