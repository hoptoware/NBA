import numpy as np
import pandas as pd

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats, playercompare

filepath1 = r"python\NBA\stats\AE_Stats.json"
filepath2 = r"python\NBA\stats\NJ_Stats.json"

id1 = players.find_players_by_full_name('Anthony Edwards')[0]['id']
id2 = players.find_players_by_full_name('Nikola Jokic')[0]['id']

comparison = playercompare.PlayerCompare(id1, id2, season='2025-26').get_data_frames()[0]
print(comparison)

