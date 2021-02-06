"""
github.com/alonzi (datascientist@virginia.edu)
class definition for the mission
2021-02-03
github.com/alonzi/currahee
this class is generator of a mission
"""

class cl_mission:

    def showFriendlies(self):
        return True

    def showFoes(self):
        return True

    def __init__(self,company,type="assault"):
        self.type = str(type)    # instance variable unique to each instance
        print("\n----> Your mission is to {}.".format(self.type))
        company.setOrders(type)

        # mission briefing from Battalion CO
        # create enemy squads
        self.enemy_squads = []

    def __del__(self):
        # debrief from Battalion CO
        print("\n----> {} MISSION ACCOMPLISHED.".format(self.type))
        
