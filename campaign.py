"""
github.com/alonzi (datascientist@virginia.edu)
class definition for the campaign
2021-02-03
github.com/alonzi/currahee
this class is the clearing house for running the game
"""

import company as co


class cl_campaign:

    #kind = 'canine'         # class variable shared by all instances

    def __init__(self, name=input("Battalion CO: come in ....?  ")):
        self.name = str(name)    # instance variable unique to each instance
        print("\n--> Hello Captain {}.".format(name))
        self.active_company = co.cl_company(name)

    def __del__(self):
        # campaign debrief
        print("\n----> Campaign Over {}.".format(self.name))

        