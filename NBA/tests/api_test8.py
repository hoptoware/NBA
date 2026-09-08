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

        selection_query = fr'''
        SELECT * FROM Zaid_Abdul_Aziz;
        '''
        cursor.execute(selection_query)

        rows = cursor.fetchall()

        duplicateIndex = None
        duplicateCounter = 0

        for i in range(1, len(rows)):
            lastRow = rows[i - 1] #compare current row to the one before it

            if rows[i][0] == lastRow[0]:
                duplicateIndex = i - 1 #index in which this duplicate group starts at
                print(f"Duplicate found at index: {duplicateIndex}")
                duplicates_found = True
                break
            else:
                pass        

        if duplicateIndex is not None: 
            for i in range(duplicateIndex, len(rows)): #from the duplicate row up until the last row
                if rows[i][0] == rows[duplicateIndex][0]: #check if their seasons are equal
                    duplicateCounter += 1 #add to the counter
                    print(rows[i])
                else:
                    break

            for i in range(duplicateIndex, duplicateIndex + duplicateCounter - 1):
                if not rows[i][1] == 'TOT': #check if the row doen't represent the total
                    delete_query = fr'''
                    DELETE FROM Zaid_Abdul_Aziz
                    WHERE season = ? AND team <> 'TOT';
                    '''
                    cursor.execute(delete_query, (rows[i][0],))
                else:
                    break
        
        connection.commit()  # Commit changes after each deletion pass
