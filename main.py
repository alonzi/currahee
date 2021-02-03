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
import my_round as rn
import company as co

def main():
    """ Main entry point of the app """
    print("\n hello world \n")

    #create campaign
    active_campaign = cm.cl_campaign()

    while(active_campaign.active_company.isAlive()):

        # company status report
        active_campaign.active_company.soundOff()
        active_campaign.active_company.materielReport()
        input("...continue...")
    
        # mission briefing
        active_mission = mi.cl_mission()
        input("...continue...")
            
        # company muster (loadout) (heavy interactive)
        active_campaign.active_company.muster() # create platoons and squads
        input("...continue...")
        
        # mission while loop (heavy interactive)
        ### while loop on cl_round (ends on overrun, objective win, retreat)
        active_campaign.active_company.LT -=1
        
        # mission debriefing
        active_mission.__del__() # doption to continue - more challenge more loot
        input("...continue...")

    # campaign debriefing (campaign destructor)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
