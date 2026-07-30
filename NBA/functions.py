import numpy as np
import pandas as pd

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
        checkDict = {'pts': None, 'reb': None, 'ast': None, 'blk': None, 'stl': None, 'tov': None}
        
        if(p1.ptsAvg > p2.ptsAvg):
            checkDict['pts'] = p1
            p1.win = p1.win + 1
        elif(p1.ptsAvg < p2.ptsAvg):
            checkDict['pts'] = p2
            p2.win = p2.win + 1
        else:
            pass

        #average rebounds result
        if(p1.rebAvg > p2.rebAvg):
            checkDict['reb'] = p1
            p1.win = p1.win + 1
        elif(p1.rebAvg < p2.rebAvg):
            checkDict['reb'] = p2
            p2.win = p2.win + 1
        else:
            pass

        #average assists result
        if(p1.astAvg > p2.astAvg):
            p1.win = p1.win + 1
            checkDict['ast'] = p1
        elif(p1.astAvg < p2.astAvg):
            checkDict['ast'] = p2
            p2.win = p2.win + 1
        else:
            pass

        #average blocks result
        if(p1.blkAvg > p2.blkAvg):
            checkDict['blk'] = p1
            p1.win = p1.win + 1
        elif(p1.blkAvg < p2.blkAvg):
            checkDict['blk'] = p2
            p2.win = p2.win + 1
        else:
            pass

        #average steals result
        if(p1.stlAvg > p2.stlAvg):
            checkDict['stl'] = p1
            p1.win = p1.win + 1
        elif(p1.stlAvg < p2.stlAvg):
            checkDict['stl'] = p2
            p2.win = p2.win + 1
        else:
            pass

        #average turnovers result
        if(p1.tovAvg > p2.tovAvg):
            checkDict['tov'] = p1
            p1.win = p1.win - 1
        elif(p1.tovAvg < p2.tovAvg):
            checkDict['tov'] = p2
            p2.win = p2.win - 1
        else:
            pass


        return [checkDict, p1.win, p2.win]
