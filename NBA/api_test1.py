import numpy as np
import pandas as pd

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats, playercompare

filepath = r"python\NBA\stats\AE_Stats.json"

id1 = players.find_players_by_full_name('Anthony Edwards')[0]['id']
id2 = players.find_players_by_full_name('Nikola Jokic')[0]['id']

careerStats1 = playercareerstats.PlayerCareerStats(id1).get_data_frames()[0]
careerStats2 = playercareerstats.PlayerCareerStats(id2).get_data_frames()

print(careerStats1)

'''with open (filepath, 'w') as stats1:
    stats1.write(careerStats1)'''