"""
github.com/alonzi (datascientist@virginia.edu)
class definition for the platoon
2021-02-03
github.com/alonzi/currahee
this class is the state of a platoon
"""



class cl_platoon:

    def isAlive(self):
        if self.LT<=0 or self.SGT<=0 or self.PVT<=0: return 0
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
        self.LT = 3
        self.SGT = 9
        self.PVT = 108

        self.ammo = 5
        self.hammo = 2
        self.radio = 3

        self.name = str(name)    # instance variable unique to each instance
        print("\n----> Your company is {}'s raiders.".format(name))
        