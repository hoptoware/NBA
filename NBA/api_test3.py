import re
import numpy as np
import pandas as pd

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats, playercompare

filepath = r"NBA\stats\AE_FullStats.json"


def get_player_data(prompt):
    while True:
        name = input(prompt).strip()
        separator_count = name.count(" ") + name.count("-")

        if not (1 <= separator_count <= 2):
            print("Try Again: the name must contain between 1 and 2 spaces or hyphens.")
            prompt = "Try Again: "
            continue

        try:
            player_id = players.find_players_by_full_name(name)[0]["id"]
            return player_id, name
        except (NameError, IndexError):
            print("Try Again: player not found.")
            prompt = "Try Again: "


id1, name1 = get_player_data("Input the first player's full name (first and last): ")
parts = [part for part in re.split(r"[\s-]+", name1) if part]

if len(parts) == 2:
    initials1 = parts[0][0].capitalize() + parts[1][0].capitalize()
elif len(parts) >= 3:
    initials1 = "".join(part[0].capitalize() for part in parts[:3])
else:
    initials1 = parts[0][0].capitalize()

name1 = players.find_player_by_id(id1)["full_name"]
print(name1)
print(initials1)

seasonStats1 = playercareerstats.PlayerCareerStats(id1).get_data_frames()[1]

with open(filepath, "w") as stats1:
    stats1.write(seasonStats1.to_json(orient="records", lines=True))
