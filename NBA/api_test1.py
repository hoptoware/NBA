import numpy as np
import pandas as pd

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats, playercompare

filepath1 = r"python\NBA\stats\AE_Stats.json"
filepath2 = r"python\NBA\stats\NJ_Stats.json"

id1 = players.find_players_by_full_name('Anthony Edwards')[0]['id']
id2 = players.find_players_by_full_name('Nikola Jokic')[0]['id']

seasonStats1 = playercareerstats.PlayerCareerStats(id1).get_data_frames()[0]
seasonStats2 = playercareerstats.PlayerCareerStats(id2).get_data_frames()[0]


'''with open (filepath1, 'w') as stats1:
    stats1.write(seasonStats1.to_json(orient='records', lines=True))

with open (filepath2, 'w') as stats2:
    stats2.write(seasonStats2.to_json(orient='records', lines=True))'''

#check for season 2025-26
for i in seasonStats1.index:
    if seasonStats1.loc[i, 'SEASON_ID'] == '2025-26':
        print(seasonStats1.loc[i])
    else:
        pass

print("\n")

for i in seasonStats2.index:
    if seasonStats2.loc[i, 'SEASON_ID'] == '2025-26':
        print(seasonStats2.loc[i])
    else:
        pass
    

#print(seasonStats1.loc[0, 'SEASON_ID'])
#print(seasonStats2)
