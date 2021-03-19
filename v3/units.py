"""
author: github.com/alonzi (datascientist@virginia.edu)
what: class definition for rifle squad, platoon HQ, and company HQ
when: 2021-03-18
where: github.com/alonzi/currahee
why: this class contains the state of a squad and its capabilities


reference: https://www.battleorder.org/us-airborne-ww2
"""

class Squad():

    def identify(self): print(self)

    def __init__(self,name="default rifle squad",PVT=10):

        self.PVT = PVT

        self.ammo = 5
        self.hammo = None

        self.AP = None
        self.orders = None
        self.in_contact = None
        self.location = None # hex index

        self.name = str(name)    # instance variable unique to each instance
        print("\n----> Unit created: {}, id = {}.".format(name,self))

class PlatoonHQ(Squad):

    def __init__(self,name="default platoon HQ",PVT=5,SGT=1):

        self.PVT = PVT
        self.SGT = SGT # in addition to inheritance from base class
        self.squads = None # list of squad pointers

        self.ammo = 5
        self.hammo = 1
        self.radio = 1 # in addition to inheritance from base class

        self.AP = None
        self.orders = None
        self.in_contact = None
        self.location = None # hex index

        self.name = str(name)    # instance variable unique to each instance
        print("\n----> Unit created: {}, id =  {}.".format(name,self))

class CompanyHQ(squad):

    def __init__(self,name="default company HQ",PVT=11,SGT=3,LTS=1):
        self.PVT = PVT
        self.SGT = SGT # in addition to inheritance from base class
        self.LTS = LTS # in addition to inheritance from base class
        self.platoons = None # list of platoon HQ pointers

        self.ammo = 10
        self.hammo = 1
        self.radio = 1 # in addition to inheritance from base class

        self.AP = None
        self.orders = None # from regiment or batallion
        self.location = None # hex index

        self.name = str(name)    # instance variable unique to each instance
        print("\n----> Unit created: {}, id =  {}.".format(name,self))
