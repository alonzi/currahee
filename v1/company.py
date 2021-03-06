"""
github.com/alonzi (datascientist@virginia.edu)
class definition for the company
2021-02-03
github.com/alonzi/currahee
this class is the game state for the player's company
"""

import platoon as pl
import squad as sq
import orders as ord

class cl_company(pl.cl_platoon):

    def setName(self,name):
        self.name = name
        return True

    def issueOrdersInFog(self):
        ''' calls issueOrders for now, will update to only work for first platoon '''
        self.issueOrders()
        return True

    def issueOrders(self):
        for platoon in self.platoons:
            platoon.soundOff()
            platoon.setOrders(platoon.chooseOrders())
        return "troops deployed"

    def choosePlatoon(self):
        return self.platoons[0]

    def distributeMateriel(self):
        for i in range(self.ammo):
            print("ammo to distribute {}".format(self.ammo))
            self.choosePlatoon().assign_ammo(1)
            self.ammo-=1
        for i in range(self.hammo):
            print("hammo to distribute {}".format(self.hammo))
            self.choosePlatoon().assign_hammo(1)
            self.hammo-=1
        for i in range(self.radio):
            print("radio to distribute {}".format(self.radio))
            self.choosePlatoon().assign_radio(1)
            self.radio-=1
        return self.soundOffMessage()
    
    def soundOffInFog(self):
        ''' calls soundOff for now, will update to only work for first platoon '''
        self.soundOff()
        return True

    def soundOffMessage(self): 
        s = super(cl_company, self).soundOffMessage()
        for platoon in self.platoons: s+=platoon.soundOffMessage()
        return s

    def soundOff(self): 
        super(cl_company, self).soundOff()
        for platoon in self.platoons: platoon.soundOff()
        return 1

    def isAlive(self):
        if self.LT<=0 or self.SGT<=0 or self.PVT<=0: return False
        else: return True

    def muster(self):
        
        for platoon in self.platoons: platoon.__del__()
        for squad in self.squads: squad.__del__()

        self.platoons = []
        self.squads = []

        for i in range(self.SGT): self.squads.append(sq.cl_squad(PVT=self.PVT//self.SGT))
        for i in range(self.LT): self.platoons.append(pl.cl_platoon())
        while(1):
            if len(self.squads)<=0:break
            for platoon in self.platoons:
                if len(self.squads)<=0:break
                platoon.assign_squad(self.squads.pop())
    
        self.soundOff()
        return self.soundOffMessage()
            
    def __init__(self, name="ALONZI"):
        self.LT = 3
        self.SGT = 9
        self.PVT = 108

        self.ammo = 5
        self.hammo = 2
        self.radio = 1

        self.platoons = []
        self.squads = []

        self.orders = ord.cl_orders()

        self.name = str(name)    # instance variable unique to each instance
        print("\n----> Your company is {}'s raiders.".format(name))
        