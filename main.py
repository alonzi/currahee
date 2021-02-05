"""
github.com/alonzi (datascientist@virginia.edu)
main program for currahee game
2021-02-03
github.com/alonzi/currahee
i was sick and watched band of brothers
"""

__author__ = "Peter Alonzi"
__version__ = "0.1.0"
__license__ = "see repo LICENSE"

import campaign as cm
import mission as mi

def main():
    """ Main entry point of the app """
    print("\n hello world \n")

    #create campaign
    active_campaign = cm.cl_campaign()

    while(active_campaign.active_company.isAlive()):
    
        # mission briefing (batallion level - receive orders)
        active_mission = mi.cl_mission(active_campaign.active_company)
        input("...continue...")
            
        # mission briefing (company level - give orders)
        # company muster (heavy interactive)
        active_campaign.active_company.muster() # create platoons and squads
        input("...continue...")
        # company distribute materiel (heavy interactive)
        active_campaign.active_company.distributeMateriel()
        input("...continue...")
        # company mission orders
        active_campaign.active_company.issueOrders()
        input("...continue...")
        # final sound off
        active_campaign.active_company.soundOff()
        input("...MOVE OUT!...")

        # mission while loop (heavy interactive)
        while(active_campaign.active_company.isAlive()):
            ### while loop on cl_round (ends on overrun, objective win, retreat)
            active_campaign.active_company.LT -=1
            input("...LT lost ... continue...")
        
        # mission debriefing
        active_mission.__del__() # doption to continue - more challenge more loot
        input("...continue...")

    # campaign debriefing (campaign destructor)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
