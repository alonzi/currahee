"""
github.com/alonzi (datascientist@virginia.edu)
class definition for the campaign
2021-02-03
github.com/alonzi/currahee
this class is the game state for the player's company
"""

class cl_company:

    #kind = 'canine'         # class variable shared by all instances
    def soundOff(self): print("currahee!")

    def __init__(self, name="ALONZI"):
        self.name = str(name)    # instance variable unique to each instance
        print("\n----> Your company is {}'s raiders.".format(name))

    