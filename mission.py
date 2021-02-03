"""
github.com/alonzi (datascientist@virginia.edu)
class definition for the campaign
2021-02-03
github.com/alonzi/currahee
this class is generator of a mission
"""

class cl_mission:

    #kind = 'canine'         # class variable shared by all instances

    def __init__(self, name="assault"):
        self.name = str(name)    # instance variable unique to each instance
        print("\n----> Your mission is to {}.".format(name))

        # briefing from Battalion CO
        # deployment orders
        # while loop on cl_round (ends on overrun, objective win, retreat)
        
        # option to continue
        # debrief from Battalion CO
