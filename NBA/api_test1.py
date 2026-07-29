import numpy as np
import pandas as pd

from functions import player

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats, playercompare


filepath1 = r"python\NBA\stats\AE_Stats.json"
filepath2 = r"python\NBA\stats\NJ_Stats.json"


#define players
id1 = players.find_players_by_full_name('Anthony Edwards')[0]['id']
id2 = players.find_players_by_full_name('Nikola Jokic')[0]['id']

#get the first dataframe of the list (which contains all career stats)
seasonStats1 = playercareerstats.PlayerCareerStats(id1).get_data_frames()[0]
seasonStats2 = playercareerstats.PlayerCareerStats(id2).get_data_frames()[0]

#save stats as json files
with open (filepath1, 'w') as stats1:
    stats1.write(seasonStats1.to_json(orient='records', lines=True))

with open (filepath2, 'w') as stats2:
    stats2.write(seasonStats2.to_json(orient='records', lines=True))

#check for season 2025-26 and print the stats for that season
for i in seasonStats1.index:
    if seasonStats1.loc[i, 'SEASON_ID'] == '2025-26':
        AE = player('Anthony Edwards', 
                    pts=float(seasonStats1.loc[i, 'PTS']), reb=float(seasonStats1.loc[i, 'REB']), ast=float(seasonStats1.loc[i, 'AST']), 
                    blk=float(seasonStats1.loc[i, 'BLK']), stl=float(seasonStats1.loc[i, 'STL']), tov=float(seasonStats1.loc[i, 'TOV']),
                    gp=float(seasonStats1.loc[i, 'GP']))
    else:
        pass

print("\n")

for i in seasonStats2.index:
    if seasonStats2.loc[i, 'SEASON_ID'] == '2025-26':
        NJ = player('Nikola Jokic', 
                    pts=float(seasonStats2.loc[i, 'PTS']), reb=float(seasonStats2.loc[i, 'REB']), ast=float(seasonStats2.loc[i, 'AST']), 
                    blk=float(seasonStats2.loc[i, 'BLK']), stl=float(seasonStats2.loc[i, 'STL']), tov=float(seasonStats2.loc[i, 'TOV']),
                    gp=float(seasonStats2.loc[i, 'GP']))
    else:
        pass
