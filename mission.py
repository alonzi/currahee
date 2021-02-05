"""
github.com/alonzi (datascientist@virginia.edu)
class definition for the mission
2021-02-03
github.com/alonzi/currahee
this class is generator of a mission
"""

class cl_mission:

    #kind = 'canine'         # class variable shared by all instances

    def __init__(self,company,type="assault"):
        self.type = str(type)    # instance variable unique to each instance
        print("\n----> Your mission is to {}.".format(self.type))
        company.setOrders(type)

        # mission briefing from Battalion CO

    def __del__(self):
        # debrief from Battalion CO
        print("\n----> {} MISSION ACCOMPLISHED.".format(self.type))
        
