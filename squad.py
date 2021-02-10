"""
github.com/alonzi (datascientist@virginia.edu)
class definition for the squad
2021-02-03
github.com/alonzi/currahee
this class is the state of a squad
"""

import orders as ord


class cl_squad:

    def setLocation(self,x,y):
        self.location = (x,y)
        return True
    
    def isAlive(self):
        if self.SGT<=0 or self.PVT<=0: return 0
        else: return 1
   
    def soundOffMessage(self):
        sound = " {} CURRAHEE!".format(self)
        status = " {} {} {} {} {} {} {}\n".format(self.LT,self.SGT,self.PVT,self.ammo,self.hammo,self.radio,self.orders.type) 
        return (sound+status)

    def soundOff(self):
        sound = "------> {} CURRAHEE!".format(self)
        status = " {} {} {} {} {} {} {}".format(self.LT,self.SGT,self.PVT,self.ammo,self.hammo,self.radio,self.orders.type) 
        print(sound+status)

    def materielReport(self):
        print("")
        print("{} rounds of ammunition".format(self.ammo))
        print("{} rounds of heavy ammo".format(self.hammo))
        print("{} radios".format(self.radio))
        print("")


    def __init__(self, name="ALONZI",PVT=4):
        self.LT = 0
        self.SGT = 1
        self.PVT = PVT

        self.ammo = 0
        self.hammo = 0
        self.radio = 0

        self.orders = ord.cl_orders()
        self.location = (2,2)

        self.name = str(name)    # instance variable unique to each instance
        print("\n----> Your squad is {}'s raiders.".format(name))

    def __del__(self):
        # debrief from Battalion CO
        print("\n----> delete squad {}.".format(self.name))

        