"""
author: github.com/alonzi (datascientist@virginia.edu)
what: class definition for the campaign state
when: 2021-03-19
where: github.com/alonzi/currahee
why: this class contains the information necessary to reconstruct the game state between missions
inspiration: the old school games like metroid where you would write down the hash for the game state
"""

class Ribbons():

    def identify(self): print(self)

    def generate_state_str(self):
        state_str = str(self.campaigns)+'-'+str(self.missions)+'-'+str(self.achievements_personal)+'-'+str(self.achievements_unit)+'-'+str(self.wounds)
        return state_str

    def __init__(self,name="default ribbon rack"):

        self.campaigns = 0
        self.missions = 0
        self.achievements_personal = 0
        self.achievements_unit = 0
        self.wounds = 0

        self.name = str(name)    # instance variable unique to each instance
        print("\n----> Ribbon rack created: {}, id = {}.".format(name,self))
