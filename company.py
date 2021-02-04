"""
github.com/alonzi (datascientist@virginia.edu)
class definition for the company
2021-02-03
github.com/alonzi/currahee
this class is the game state for the player's company
"""

import platoon as pl
import squad as sq

class cl_company(pl.cl_platoon):

    def soundOff(self): 
        print("COMPANY {} CURRAHEE! STRENGTH {}".format(self,self.PVT))
        for platoon in self.platoons: platoon.soundOff()

    def isAlive(self):
        if self.LT<=0 or self.SGT<=0 or self.PVT<=0: return 0
        else: return 1

    def muster(self):
        
        for platoon in self.platoons: platoon.__del__()
        for squad in self.squads: squad.__del__()

        for i in range(self.SGT): self.squads.append(sq.cl_squad(PVT=self.PVT//self.SGT))
        for i in range(self.LT): self.platoons.append(pl.cl_platoon())
        while(1):
            if len(self.squads)<=0:break
            for platoon in self.platoons:
                if len(self.squads)<=0:break
                platoon.assign_squad(self.squads.pop())
        return 1
            
    def __init__(self, name="ALONZI"):
        self.LT = 3
        self.SGT = 9
        self.PVT = 108

        self.ammo = 5
        self.hammo = 2
        self.radio = 1

        self.platoons = []
        self.squads = []

        self.name = str(name)    # instance variable unique to each instance
        print("\n----> Your company is {}'s raiders.".format(name))
        