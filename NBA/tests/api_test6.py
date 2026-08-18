import sqlite3

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats


player_name = 'Carmelo Anthony'
player_id = players.find_players_by_full_name(player_name)[0]["id"]
seasonStats1 = playercareerstats.PlayerCareerStats(player_id).get_data_frames()[0]

player_name = player_name.replace(' ', '_')

initials = 'CA'
filepath = fr"NBA\stats\playersStats.db"

with sqlite3.connect(filepath) as connection:
    cursor = connection.cursor()

    cursor.execute(fr'''
    CREATE TABLE IF NOT EXISTS {player_name} 
    (season REAL,
    ppg REAL,
    rpg REAL,
    apg REAL
    );
    ''')

    insert_query = fr'''
    INSERT INTO {player_name} (season, ppg, rpg, apg) 
    VALUES (?, ?, ?, ?);
    '''

    for i in seasonStats1.index:
        values = (seasonStats1.iloc[i,1], round(float(seasonStats1.loc[i, 'PTS'] / seasonStats1.loc[i, 'GP']), 1), 
                  round(float(seasonStats1.loc[i, 'REB'] / seasonStats1.loc[i, 'GP']), 1), 
                  round(float(seasonStats1.loc[i, 'AST'] / seasonStats1.loc[i, 'GP']), 1))
        cursor.execute(insert_query, values)

    connection.commit()

print(seasonStats1)
print(seasonStats1.loc[i, 'PTS'])