import numpy as np
import pandas as pd

class player:
    def __init__(self, name, 
                 pts = None, reb = None, ast = None, 
                 blk = None, stl = None, tov = None,
                 gp = None):
        
        self.name = name
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