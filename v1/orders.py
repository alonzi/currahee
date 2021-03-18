"""
github.com/alonzi (datascientist@virginia.edu)
class definition for the orders
2021-02-03
github.com/alonzi/currahee
this class is the orders a platoon has
"""

class cl_orders:

    def execute(self):
        ''' this is what happens when the squad acts '''
        print("... ececuting orders ... {}".format(self.type))
        return True

    def __init__(self,type="fire"):
        ''' on construction player selects orders '''
                # turn in into loop over list of orders that is build by possibilities
#        print("1. advance")
#        print("2. fall back")
#        print("3. take cover")
#        print("4. supressive fire")
#        print("5. heavy fire")
#        print("6. retreat")

        self.type = type
        print("orders given")

    def __del__(self):
        print("orders deleted")
