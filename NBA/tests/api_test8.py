import sqlite3
from pathlib import Path

import pandas as pd

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats


datapath = Path(__file__).resolve().parent.parent / "stats" / "playersStats.db"


with sqlite3.connect(datapath) as connection:
    cursor = connection.cursor()

    duplicates_found = True
    
    while duplicates_found:
        duplicates_found = False
        breakLoop = False

        selection_query = fr'''
        SELECT * FROM Zaid_Abdul_Aziz;
        '''
        cursor.execute(selection_query)

        rows = cursor.fetchall()

        duplicate_season = None

        for row in range(1, len(rows)):
            lastRow = rows[row - 1]

            if rows[row][0] == lastRow[0]:
                duplicate_season = rows[row][0]
                print(f"Duplicate found for season: {duplicate_season}")
                duplicates_found = True
                break

        if duplicate_season is not None:
            delete_query = fr'''
            DELETE FROM Zaid_Abdul_Aziz
            WHERE season = ? AND team <> 'TOT';
            '''
            cursor.execute(delete_query, (duplicate_season,))
        
        connection.commit()  # Commit changes after each deletion pass
