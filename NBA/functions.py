import pandas as pd
import re

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats, playercompare


class player:
    def __init__(self, name, 
                 pts = None, reb = None, ast = None, 
                 blk = None, stl = None, tov = None,
                 gp = None):
        
        self.name = name
        self.short = ' '

        self.pts = pts
        self.reb = reb
        self.ast = ast
        self.blk = blk
        self.stl = stl
        self.tov = tov
        self.gp = gp

        self.ptsAvg = round(self.pts / self.gp, 1) if self.gp else None
        self.rebAvg = round(self.reb / self.gp, 1) if self.gp else None
        self.astAvg = round(self.ast / self.gp, 1) if self.gp else None
        self.blkAvg = round(self.blk / self.gp, 1) if self.gp else None
        self.stlAvg = round(self.stl / self.gp, 1) if self.gp else None
        self.tovAvg = round(self.tov / self.gp, 1) if self.gp else None


    def compare(p1, p2): #arguments must be of the class 'player'
        p1.win = 0
        p2.win = 0
        checkDict = {'pts': '??', 'reb': '??', 'ast': '??', 'blk': '??', 'stl': '??', 'tov': '??'}
        
        if(p1.ptsAvg > p2.ptsAvg):
            checkDict['pts'] = '<='
            p1.win = p1.win + 1
        elif(p1.ptsAvg < p2.ptsAvg):
            checkDict['pts'] = '=>'
            p2.win = p2.win + 1
        else:
            checkDict['pts'] = '=='

        #average rebounds result
        if(p1.rebAvg > p2.rebAvg):
            checkDict['reb'] = '<='
            p1.win = p1.win + 1
        elif(p1.rebAvg < p2.rebAvg):
            checkDict['reb'] = '=>'
            p2.win = p2.win + 1
        else:
            checkDict['reb'] = '=='

        #average assists result
        if(p1.astAvg > p2.astAvg):
            p1.win = p1.win + 1
            checkDict['ast'] = '<='
        elif(p1.astAvg < p2.astAvg):
            checkDict['ast'] = '=>'
            p2.win = p2.win + 1
        else:
            checkDict['ast'] = '=='

        #average blocks result
        if(p1.blkAvg > p2.blkAvg):
            checkDict['blk'] = '<='
            p1.win = p1.win + 1
        elif(p1.blkAvg < p2.blkAvg):
            checkDict['blk'] = '=>'
            p2.win = p2.win + 1
        else:
            checkDict['blk'] = '=='

        #average steals result
        if(p1.stlAvg > p2.stlAvg):
            checkDict['stl'] = '<='
            p1.win = p1.win + 1
        elif(p1.stlAvg < p2.stlAvg):
            checkDict['stl'] = '=>'
            p2.win = p2.win + 1
        else:
            checkDict['stl'] = '=='

        #average turnovers result
        if(p1.tovAvg > p2.tovAvg):
            checkDict['tov'] = '<='
            p1.win = p1.win - 1
        elif(p1.tovAvg < p2.tovAvg):
            checkDict['tov'] = '=>'
            p2.win = p2.win - 1
        else:
            checkDict['tov'] = '=='


        return [checkDict, p1.win, p2.win]


    def findPlayer(num):
        if num == 1:
            prompt = "Input the first player's full name (first and last): "
        elif num == 2:
            prompt = "Input the second player's full name (first and last): "


        while True:
            name = input(prompt).strip().replace('.', '')
            name = ' '.join(name.split())
            name = ' '.join(name.split(sep = '-'))
            separator_count = name.count(" ") + name.count("-")

            if not (1 <= separator_count <= 2):
                prompt = "Try Again: "
                continue

            try:
                player_id = players.find_players_by_full_name(name)[0]["id"] 
                break
            except (NameError, IndexError):
                prompt = "Player not found. Try Again: "

        name = players.find_player_by_id(player_id)['full_name']

        initials = ''.join(re.findall(r'(?:^|[ -])([A-Za-z])', name)).upper()

        return {'id': player_id, 'initials': initials, 'name': name}
