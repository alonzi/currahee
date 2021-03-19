"""
author: github.com/alonzi (datascientist@virginia.edu)
what: class definition for rifle squad
when: 2021-03-18
where: github.com/alonzi/currahee
why: this class contains the state of a squad and its capabilities


reference: https://www.battleorder.org/us-airborne-ww2
"""

class Squad():

    def identify(self): print(self)

    def __init__(self,name="default squad",PVT=11):
        self.PVT = PVT
        self.AP = 2
        self.ammo = 5
        self.hammo = 1
        self.radio = 1
        self.orders = None
        self.in_contact = True
        self.location = None (hex index)
        self.name = str(name)    # instance variable unique to each instance
        print("\n----> Squad created: {}'s raiders.".format(name))