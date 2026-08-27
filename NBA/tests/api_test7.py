import sqlite3
from pathlib import Path

import re
import numpy as np
import pandas as pd

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats


id1 = players.find_players_by_full_name('Anthony Edwards')[0]["id"]
seasonStats1 = playercareerstats.PlayerCareerStats(id1).get_data_frames()[0]


#player1 = players.find_player_by_id(id1)
#playerName = players.find_player_by_id(id1)['full_name']

playerName = "  C.J.     McCollum "
name = playerName.strip().replace('.', '')
name = ' '.join(name.split())
name = ' '.join(name.split(sep = '-'))

separator_count = name.count(" ") + name.count("-")

print(name)
print(separator_count)