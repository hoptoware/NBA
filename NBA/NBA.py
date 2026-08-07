import numpy as np
import pandas as pd

from functions import player

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats


whitespace = " "

name1 = ""
name2 = ""


##########


print("NBA PLAYER COMPARISON (25-26 season)\n")

#define players
player1 = player.findPlayer(1)
player2 = player.findPlayer(2)

id1 = player1['id']
id2 = player2['id']

filepath1 = fr"NBA\stats\{player1['initials']}_Stats.json" #these paths might not always work
filepath2 = fr"NBA\stats\{player2['initials']}_Stats.json"

#get the first dataframe of the list (which contains all career stats)
seasonStats1 = playercareerstats.PlayerCareerStats(id1).get_data_frames()[0]
seasonStats2 = playercareerstats.PlayerCareerStats(id2).get_data_frames()[0]

#save stats as json files
try:
    with open (filepath1, 'r') as stats1:
        pass #check for file
    filepath1 = fr"NBA\stats\{player1['initials']}_Stats1.json"
    with open (filepath1, 'w') as stats1:
        stats1.write(seasonStats1.to_json(orient='records', lines=True)) #if exists, write with another name
except: #if doesn't exist
    with open (filepath1, 'w') as stats1:
        stats1.write(seasonStats1.to_json(orient='records', lines=True)) #save it with default name

try:
    with open (filepath2, 'r') as stats2:
        pass #check for file
    filepath2 = fr"NBA\stats\{player2['initials']}_Stats1.json"
    with open (filepath2, 'w') as stats2:
        stats2.write(seasonStats2.to_json(orient='records', lines=True)) #if exists, write with another name
except: #if doesn't exist
    with open (filepath2, 'w') as stats2:
        stats2.write(seasonStats2.to_json(orient='records', lines=True)) #save it with default name

#check for season 2025-26 and print the stats for that season
for i in seasonStats1.index:
    if seasonStats1.loc[i, 'SEASON_ID'] == '2025-26':
        P1 = player(player1['name'], 
                    pts=float(seasonStats1.loc[i, 'PTS']), reb=float(seasonStats1.loc[i, 'REB']), ast=float(seasonStats1.loc[i, 'AST']), 
                    blk=float(seasonStats1.loc[i, 'BLK']), stl=float(seasonStats1.loc[i, 'STL']), tov=float(seasonStats1.loc[i, 'TOV']),
                    gp=float(seasonStats1.loc[i, 'GP']))
    else:
        pass

print("\n")

for i in seasonStats2.index:
    if seasonStats2.loc[i, 'SEASON_ID'] == '2025-26':
        P2 = player(player2['name'], 
                    pts=float(seasonStats2.loc[i, 'PTS']), reb=float(seasonStats2.loc[i, 'REB']), ast=float(seasonStats2.loc[i, 'AST']), 
                    blk=float(seasonStats2.loc[i, 'BLK']), stl=float(seasonStats2.loc[i, 'STL']), tov=float(seasonStats2.loc[i, 'TOV']),
                    gp=float(seasonStats2.loc[i, 'GP']))
    else:
        pass

#TODO: add an exception in case the player doesn't have stats in 2025-26 season
comparison = player.compare(P1, P2)

print("2025-26 STATS")
print(f"{name1} vs. {name2}: (Arrow points the category winner)")


#points result
#TODO: centralize the text
print(f"----------POINTS----------\n {player1['initials']}: {P1.ptsAvg} {comparison[0]['pts']} {P2.ptsAvg} :{player2['initials']}")
print(f"----------REBOUNDS----------\n {player1['initials']}: {P1.rebAvg} {comparison[0]['reb']} {P2.rebAvg} :{player2['initials']}")
print(f"----------ASSISTS----------\n {player1['initials']}: {P1.astAvg} {comparison[0]['ast']} {P2.astAvg} :{player2['initials']}")
print(f"----------BLOCKS----------\n {player1['initials']}: {P1.blkAvg} {comparison[0]['blk']} {P2.blkAvg} :{player2['initials']}")
print(f"----------STEALS----------\n {player1['initials']}: {P1.stlAvg} {comparison[0]['stl']} {P2.stlAvg} :{player2['initials']}")
print(f"----------TURNOVERS----------\n {player1['initials']}: {P1.tovAvg} {comparison[0]['tov']} {P2.tovAvg} :{player2['initials']}")

if comparison[1] > comparison[2]:
    print(f"\nOVERALL WINNER: {P1.name}")
elif comparison[1] < comparison[2]:
    print(f"\nOVERALL WINNER: {P2.name}")
else:
    print("\nTIE")
