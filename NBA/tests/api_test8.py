import sqlite3
from pathlib import Path

import pandas as pd

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats


datapath = Path(__file__).resolve().parent.parent / "stats" / "playersStats.db"


with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()

        selection_query = fr'''
        SELECT * FROM Zaid_Abdul_Aziz;
        '''
        cursor.execute(selection_query)

        rows = cursor.fetchall()

        duplicate = None
        duplicateCounter = 0

        for row in range(1, len(rows)):
            lastRow = rows[row - 1]

            if rows[row][0] == lastRow[0]:
                duplicate = row - 1
                print(duplicate)
                break
            else:
                pass        

        if duplicate is not None:
            for row in rows:
                if row[0] == rows[duplicate][0]:
                    duplicateCounter += 1
                    print(row)
                elif not row[0] == rows[duplicate][0]:
                    break

            for row in range(duplicateCounter - 1):
                if not rows[duplicate + row][1] == 'TOT':
                    delete_query = fr'''
                    DELETE FROM Zaid_Abdul_Aziz
                    WHERE season = ? AND team = ?;
                    '''
                    cursor.execute(delete_query, (rows[duplicate + row][0], rows[duplicate + row][1]))
                else:
                    break

    #TODO: make code run until there are no more duplicate seasons in the table