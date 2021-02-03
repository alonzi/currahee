"""
github.com/alonzi (datascientist@virginia.edu)
class definition for the company
2021-02-03
github.com/alonzi/currahee
this class is the game state for the player's company
"""

import platoon as pl

class cl_company(pl.cl_platoon):

    #kind = 'canine'         # class variable shared by all instances
    def muster(self):
        print("\n make a platoon") # use platoon constructor
        return 1
            
    def __init__(self, name="ALONZI"):
        self.LT = 3
        self.SGT = 9
        self.PVT = 108

        self.ammo = 5
        self.hammo = 2
        self.radio = 3

        self.name = str(name)    # instance variable unique to each instance
        print("\n----> Your company is {}'s raiders.".format(name))
        