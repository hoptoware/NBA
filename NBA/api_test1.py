import numpy as np
import pandas as pd

from functions import player

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats


whitespace = " "

name1 = ""
name2 = ""


##########


print("NBA PLAYER COMPARISON\n")

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

name2 = input("Input the second player's full name (first and last): ")
if name2.count(" ") + name2.count("-") == 0:
    name2 = input("Try Again: ")
    while name2.count(" ") + name2.count("-") == 0:
        name2 = input("Try Again: ")
elif name2.count(" ") + name2.count("-") == 1:
    initials2 = name2[0].capitalize() + name2[name2.find(" ") + 1].capitalize()
elif name2.count(" ") + name2.count("-") == 2:
    initials2 = name2[0].capitalize() + name2[name2.find(" ") + 1].capitalize() + name2[-name2.find(" ") - 1].capitalize()
else:
    name2 = input("Try Again: ")
    while name2.count(" ") + name2.count("-") == 0:
        name2 = input("Try Again: ")

filepath1 = fr"NBA\stats\{initials1}_Stats.json" #these paths might not always work
filepath2 = fr"NBA\stats\{initials2}_Stats.json"

#define players
id1 = players.find_players_by_full_name(name1)[0]['id']
id2 = players.find_players_by_full_name(name2)[0]['id']

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
        P1 = player(name1, 
                    pts=float(seasonStats1.loc[i, 'PTS']), reb=float(seasonStats1.loc[i, 'REB']), ast=float(seasonStats1.loc[i, 'AST']), 
                    blk=float(seasonStats1.loc[i, 'BLK']), stl=float(seasonStats1.loc[i, 'STL']), tov=float(seasonStats1.loc[i, 'TOV']),
                    gp=float(seasonStats1.loc[i, 'GP']))
    else:
        pass

print("\n")

for i in seasonStats2.index:
    if seasonStats2.loc[i, 'SEASON_ID'] == '2025-26':
        P2 = player(name2, 
                    pts=float(seasonStats2.loc[i, 'PTS']), reb=float(seasonStats2.loc[i, 'REB']), ast=float(seasonStats2.loc[i, 'AST']), 
                    blk=float(seasonStats2.loc[i, 'BLK']), stl=float(seasonStats2.loc[i, 'STL']), tov=float(seasonStats2.loc[i, 'TOV']),
                    gp=float(seasonStats2.loc[i, 'GP']))
    else:
        pass


comparison = player.compare(P1, P2)

print("2025-26 STATS")
print(f"{name1} vs. {name2}: (Arrow points the category winner)")


#points result
print(f"----------POINTS----------\n {initials1}: {P1.ptsAvg} {comparison[0]['pts']} {P2.ptsAvg} :{initials2}")
print(f"----------REBOUNDS----------\n {initials1}: {P1.rebAvg} {comparison[0]['reb']} {P2.rebAvg} :{initials2}")
print(f"----------ASSISTS----------\n {initials1}: {P1.astAvg} {comparison[0]['ast']} {P2.astAvg} :{initials2}")
print(f"----------BLOCKS----------\n {initials1}: {P1.blkAvg} {comparison[0]['blk']} {P2.blkAvg} :{initials2}")
print(f"----------STEALS----------\n {initials1}: {P1.stlAvg} {comparison[0]['stl']} {P2.stlAvg} :{initials2}")
print(f"----------TURNOVERS----------\n {initials1}: {P1.tovAvg} {comparison[0]['tov']} {P2.tovAvg} :{initials2}")

if comparison[1] > comparison[2]:
    print(f"\nOVERALL WINNER: {P1.name}")
elif comparison[1] < comparison[2]:
    print(f"\nOVERALL WINNER: {P2.name}")
else:
    print("\nTIE")

#TODO: add a try except block to catch errors when the player name is not found in the database.
