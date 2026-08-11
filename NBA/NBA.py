import numpy as np
import pandas as pd

from functions import player

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats


whitespace = " "


##########


print("NBA PLAYER COMPARISON (25-26 season)\n")



player1 = player.findPlayer(1)
id1 = player1['id']
filepath1 = fr"NBA\stats\{player1['initials']}_Stats.json" #these filepaths might not work on other computers
seasonStats1 = playercareerstats.PlayerCareerStats(id1).get_data_frames()[0] #get the first dataframe of the list (which contains all career stats)

try:
    with open (filepath1, 'r') as stats:
        pass #check for file
    for i in range(1, 9999):
        try:
            filepath1 = fr"NBA\stats\{player1['initials']}_Stats{i}.json"
            with open (filepath1, 'r') as stats:
                pass #check for file
        except:
            with open (filepath1, 'w') as stats:
                stats.write(seasonStats1.to_json(orient='records', lines=True)) #if exists, write with another name
            break #if file doesn't exist, break the loop and save it with that name      
except: #if doesn't exist
    with open (filepath1, 'w') as stats:
        stats.write(seasonStats1.to_json(orient='records', lines=True)) #save it with default name

#check for season 2025-26 and print the stats for that season
for i in seasonStats1.index:
    if seasonStats1.loc[i, 'SEASON_ID'] == '2025-26':
        P1 = player(player1['name'], 
                    pts=float(seasonStats1.loc[i, 'PTS']), reb=float(seasonStats1.loc[i, 'REB']), ast=float(seasonStats1.loc[i, 'AST']), 
                    blk=float(seasonStats1.loc[i, 'BLK']), stl=float(seasonStats1.loc[i, 'STL']), tov=float(seasonStats1.loc[i, 'TOV']),
                    gp=float(seasonStats1.loc[i, 'GP']))
        break
    else:
        P1 = None



player2 = player.findPlayer(2)
id2 = player2['id']
filepath2 = fr"NBA\stats\{player2['initials']}_Stats.json"
seasonStats2 = playercareerstats.PlayerCareerStats(id2).get_data_frames()[0]

try:
    with open (filepath2, 'r') as stats:
        pass #check for file
    for i in range(1, 9999):
        try:
            filepath2 = fr"NBA\stats\{player2['initials']}_Stats{i}.json"
            with open (filepath2, 'r') as stats:
                pass #check for file
        except:
            with open (filepath2, 'w') as stats:
                stats.write(seasonStats2.to_json(orient='records', lines=True)) #if exists, write with another name
            break #if file doesn't exist, break the loop and save it with that name      
except: #if doesn't exist
    with open (filepath2, 'w') as stats:
        stats.write(seasonStats2.to_json(orient='records', lines=True)) #save it with default name

for i in seasonStats2.index:
    if seasonStats2.loc[i, 'SEASON_ID'] == '2025-26':
        P2 = player(player2['name'], 
                    pts=float(seasonStats2.loc[i, 'PTS']), reb=float(seasonStats2.loc[i, 'REB']), ast=float(seasonStats2.loc[i, 'AST']), 
                    blk=float(seasonStats2.loc[i, 'BLK']), stl=float(seasonStats2.loc[i, 'STL']), tov=float(seasonStats2.loc[i, 'TOV']),
                    gp=float(seasonStats2.loc[i, 'GP']))
        break
    else:
        P2 = None



#print results
if P1 == None:
    print(f"{player1['name']} hasn't played in the 2025-26 season. The comparison cannot be made.")
elif P2 == None:
    print(f"{player2['name']} hasn't played in the 2025-26 season. The comparison cannot be made.")
else:
    comparison = player.compare(P1, P2)

    print("2025-26 STATS")
    print(f"{player1['name']} vs. {player2['name']}: (Arrow points the category winner)")

    print(f"{int((20 - len("POINTS"))/2)*whitespace} POINTS {int((20 - len("POINTS"))/2)*whitespace}" + f"\n {player1['initials']}: {P1.ptsAvg} {comparison[0]['pts']} {P2.ptsAvg} :{player2['initials']}")
    print(f"{int((18 - len("REBOUNDS"))/2)*whitespace} REBOUNDS {int((18 - len("REBOUNDS"))/2)*whitespace}" + f"\n {player1['initials']}: {P1.rebAvg} {comparison[0]['reb']} {P2.rebAvg} :{player2['initials']}")
    print(f"{int((18 - len("ASSISTS"))/2)*whitespace} ASSISTS {int((18)/2)*whitespace}" + f"\n {player1['initials']}: {P1.astAvg} {comparison[0]['ast']} {P2.astAvg} :{player2['initials']}")
    print(f"{int((18 - len("BLOCKS"))/2)*whitespace} BLOCKS {int((18 - len("BLOCKS"))/2)*whitespace}" + f"\n {player1['initials']}: {P1.blkAvg} {comparison[0]['blk']} {P2.blkAvg} :{player2['initials']}")
    print(f"{int((18 - len("STEALS"))/2)*whitespace} STEALS {int((18 - len("STEALS"))/2)*whitespace}" + f"\n {player1['initials']}: {P1.stlAvg} {comparison[0]['stl']} {P2.stlAvg} :{player2['initials']}")
    print(f"{int((18 - len("TURNOVERS"))/2)*whitespace} TURNOVERS {int((18 - len("TURNOVERS"))/2)*whitespace}" + f"\n {player1['initials']}: {P1.tovAvg} {comparison[0]['tov']} {P2.tovAvg} :{player2['initials']}")

    if comparison[1] > comparison[2]:
        print(f"\nOVERALL WINNER: {P1.name}")
    elif comparison[1] < comparison[2]:
        print(f"\nOVERALL WINNER: {P2.name}")
    else:
        print("\nTIE")
