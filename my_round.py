"""
github.com/alonzi (datascientist@virginia.edu)
class definition for the campaign
2021-02-03
github.com/alonzi/currahee
this class is generator of a round
"""

class cl_round:

    #kind = 'canine'         # class variable shared by all instances

    def __init__(self, name=1):
        self.name = str(name)    # instance variable unique to each instance
        print("\n------> Round {}.".format(name))

        # get intel / give orders
        # resolve orders
