"""
author: github.com/alonzi (datascientist@virginia.edu)
what: class definition for the mission state
when: 2021-03-19
where: github.com/alonzi/currahee
why: this class contains the information necessary to reconstruct the mission state during gameplay
"""

class Mission():

    def identify(self): print(self)

    def __init__(self,name="default mission"):

        self.mission_ID = 0

        self.name = str(name)    # instance variable unique to each instance
        print("\n----> Ribbon rack created: {}, id = {}.".format(name,self))
