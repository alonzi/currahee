"""
github.com/alonzi (datascientist@virginia.edu)
class definition for the campaign
2021-02-03
github.com/alonzi/currahee
this class is the clearing house for running the game
"""

import company as co

class cl_campaign:

    def __new__(self, name=input("Battalion CO: come in ....?  ")):
        print("\n--> Hello Captain {} welcome to the campaign.".format(name))
        self.active_company = co.cl_company(name)
        return self,self.active_company

    def __del__(self):
        # campaign debrief
        print("\n----> Campaign Over {}.".format(self.name))

        