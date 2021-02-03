"""
github.com/alonzi (datascientist@virginia.edu)
class definition for the squad
2021-02-03
github.com/alonzi/currahee
this class is the state of a squad
"""

class cl_squad:

    def isAlive(self):
        if self.SGT<=0 or self.PVT<=0: return 0
        else: return 1
   
    def soundOff(self): 
        print("{} CURRAHEE!".format(self.PVT))
        print("{} CURRAHEE!".format(self.PVT))

    def materielReport(self):
        print("")
        print("{} rounds of ammunition".format(self.ammo))
        print("{} rounds of heavy ammo".format(self.hammo))
        print("{} radios".format(self.radio))
        print("")


    def __init__(self, name="ALONZI"):
        self.SGT = 0
        self.PVT = 0

        self.ammo = 0
        self.hammo = 0
        self.radio = 0

        self.name = str(name)    # instance variable unique to each instance
        print("\n----> Your squad is {}'s raiders.".format(name))
        