import sqlite3

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats


player_name = 'Carmelo Anthony'
player_id = players.find_players_by_full_name(player_name)[0]["id"]
seasonStats1 = playercareerstats.PlayerCareerStats(player_id).get_data_frames()[0]

player_name = player_name.replace(' ', '_')

initials = 'CA'
filepath = fr"NBA\stats\playersStats.db"


try:
    with open (filepath, 'r') as stats:
        pass #make sure database exists
except:
    with open (filepath, 'w') as stats:
        pass


try:
    with sqlite3.connect(filepath) as connection:
        cursor = connection.cursor()

        selection_query = fr'''
        SELECT * FROM {player_name};
        '''

        cursor.execute(selection_query)

        all_students = cursor.fetchall()

        
        update_query = fr'''
            UPDATE {player_name} 
            SET ppg = ?,
                rpg = ?,
                apg = ?,
                bpg = ?,
                spg = ?,
                tovpg = ?
            WHERE season = ?;
            '''

        for i in seasonStats1.index:
            values = (
                    round(float(seasonStats1.loc[i, 'PTS'] / seasonStats1.loc[i, 'GP']), 1), 
                    round(float(seasonStats1.loc[i, 'REB'] / seasonStats1.loc[i, 'GP']), 1), 
                    round(float(seasonStats1.loc[i, 'AST'] / seasonStats1.loc[i, 'GP']), 1),
                    round(float(seasonStats1.loc[i, 'BLK'] / seasonStats1.loc[i, 'GP']), 1),
                    round(float(seasonStats1.loc[i, 'STL'] / seasonStats1.loc[i, 'GP']), 1),  
                    round(float(seasonStats1.loc[i, 'TOV'] / seasonStats1.loc[i, 'GP']), 1),
                    seasonStats1.loc[i, 'SEASON_ID'])
            cursor.execute(update_query, values)


        print("table updated")
except:
        with sqlite3.connect(filepath) as connection:
            cursor = connection.cursor()

            cursor.execute(fr'''
            CREATE TABLE IF NOT EXISTS {player_name} 
            (season REAL,
            ppg REAL,
            rpg REAL,
            apg REAL,
            bpg REAL,
            spg REAL,
            tovpg REAL
            );
            ''')

            insert_query = fr'''
            INSERT INTO {player_name} (season, ppg, rpg, apg, bpg, spg, tovpg) 
            VALUES (?, ?, ?, ?, ?, ?, ?);
            '''

            for i in seasonStats1.index:
                values = (seasonStats1.loc[i, 'SEASON_ID'], 
                        round(float(seasonStats1.loc[i, 'PTS'] / seasonStats1.loc[i, 'GP']), 1), 
                        round(float(seasonStats1.loc[i, 'REB'] / seasonStats1.loc[i, 'GP']), 1), 
                        round(float(seasonStats1.loc[i, 'AST'] / seasonStats1.loc[i, 'GP']), 1),
                        round(float(seasonStats1.loc[i, 'BLK'] / seasonStats1.loc[i, 'GP']), 1),
                        round(float(seasonStats1.loc[i, 'STL'] / seasonStats1.loc[i, 'GP']), 1),  
                        round(float(seasonStats1.loc[i, 'TOV'] / seasonStats1.loc[i, 'GP']), 1))
                cursor.execute(insert_query, values)

            connection.commit()


            print("table created or not found")
