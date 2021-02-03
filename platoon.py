"""
github.com/alonzi (datascientist@virginia.edu)
class definition for the platoon
2021-02-03
github.com/alonzi/currahee
this class is the state of a platoon
"""

import squad as sq

class cl_platoon(sq.cl_squad):

    def muster(self):
        print("\n make a squad ") # use squad constructor
        return squads

    def isAlive(self):
        if self.LT<=0 or self.SGT<=0 or self.PVT<=0: return 0
        else: return 1


    def __init__(self, name="ALONZI"):
        self.LT = 0
        self.SGT = 0
        self.PVT = 0

        self.ammo = 0
        self.hammo = 0
        self.radio = 0

        self.name = str(name)    # instance variable unique to each instance
        print("\n----> Your platoon is {}'s raiders.".format(name))
        