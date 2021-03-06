"""
github.com/alonzi (datascientist@virginia.edu)
main program for currahee game
2021-02-03
github.com/alonzi/currahee
i was sick and watched band of brothers
"""

# requires python3.7 or greater
# requires random and chess

__author__ = "Peter Alonzi"
__version__ = "0.1.0"
__license__ = "see repo LICENSE"

import campaign as cm
import mission as mi

import random
import chess
import viz

import tkinter as tk


def main():
    """ Main entry point of the app """
    print("\n hello world \n")

    # create the viz class
    p_viz = viz.cl_viz()    

    #create campaign
    (active_campaign,active_company) = cm.cl_campaign()

    prompt = "Batallion CO: Come in captain, welcome to the regiment. What's  your name?"
    var2set = "Last Name"
    active_company.setName(p_viz.request(prompt,var2set))

    while(active_company.isAlive()):
    
        # mission briefing (batallion level - receive orders)
        active_mission = mi.cl_mission(active_company,p_viz)
            
        # mission briefing (company level - give orders)
        # company muster (heavy interactive)
        message = active_company.muster() # create platoons and squads
        p_viz.setScoreBoard(active_company.LT,active_company.SGT,active_company.PVT)
        p_viz.showMap(message)

        # company distribute materiel (heavy interactive)
        message = active_company.distributeMateriel()
        message = "assign materiel \n"+message
        p_viz.showMap(message)

        # company mission orders (heavy interactive)
        for platoon in active_company.platoons:
            platoon.orders.type = p_viz.showMap("Where to deploy {} ".format(platoon))


        ## add friendlies to board - squads assigned auto by their LT
        for platoon in active_company.platoons:
            for squad in platoon.squads:
                squad.setLocation(platoon.orderSquad())
                active_mission.addSquadFriend(squad)
                
        active_mission.renderBoard()
        p_viz.showMap("should see all squads")#active_company.soundOffMessage())


        # mission while loop (heavy interactive)
        while(active_company.isAlive()):
            
            # build active_squads_friends
            active_squads_friends = []
            for platoon in active_company.platoons: 
                for squad in platoon.squads:
                    active_squads_friends.append(squad)

            # build active_squads_foes
            active_squads_foes = []
            for squad in active_mission.enemy_squads: 
                active_squads_foes.append(squad)
            
            ### while loop on cl_round (ends when one side is eliminated/surrender/retreats, nb: you can do your objective and retreat and win)

            # remove squads from board

            # show friendly troops on map
            active_mission.showFriendlies(active_squads_friends) 
            p_viz.showMap("now with friendlies")


            # reveal enemy squads
            active_mission.showFoes(active_squads_foes) 
            
            # execute orders
            active_squads = active_squads_friends+active_squads_foes
            random.shuffle(active_squads)
            for squad in active_squads: 
                squad.orders.execute() 
            active_company.LT -=1  # casualty simulation for debugging only
            input("...LT lost ... continue...")

            # sound off with fog of war
            active_company.soundOffInFog()

            # revise orders
            active_company.issueOrdersInFog()

            
        
        # mission debriefing
        active_mission.__del__() # doption to continue - more challenge more loot
        input("...continue...")

    # campaign debriefing (campaign destructor)
    #active_campaign.__del__() # bugs saying it wasn't instantiated


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
