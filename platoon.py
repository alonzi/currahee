"""
github.com/alonzi (datascientist@virginia.edu)
class definition for the platoon
2021-02-03
github.com/alonzi/currahee
this class is the state of a platoon
"""

import squad as sq

class cl_platoon(sq.cl_squad):

    def chooseOrders(self):
        return input("...give orders --> ")

    def setOrders(self,orders):
        self.orders = orders
        return True

    def issueOrders(self):
        return True

    def soundOff(self): 
        super(cl_platoon, self).soundOff()
        for squad in self.squads: squad.soundOff()
        return True
        
    def assign_ammo(self,x):
        self.ammo+=x
        return True
        
    def assign_hammo(self,x):
        self.hammo+=x
        return True
        
    def assign_radio(self,x):
        self.radio+=x
        return True
        
    def assign_squad(self,squad):
        # add in something to catch a null squad
        self.squads.append(squad)
        self.SGT+=1
        self.PVT+=squad.PVT
        return 1

    def isAlive(self):
        if self.LT<=0 or self.SGT<=0 or self.PVT<=0: return 0
        else: return 1

    def __init__(self, name="ALONZI"):
        self.LT = 1
        self.SGT = 0
        self.PVT = 0

        self.ammo = 0
        self.hammo = 0
        self.radio = 0

        self.orders = []

        self.squads = []

        self.name = str(name)    # instance variable unique to each instance
        print("\n----> Your platoon is {}'s raiders.".format(name))
        
    def __del__(self):
        # debrief from Battalion CO
        print("\n----> delete platoon {}.".format(self.name))
