# imports
# -------
import time
import random

# variables
# ---------
t = 0  # used for timing on the countdowns
ts = 0  # (use variable as 1 for submission)used for timing on time.sleep so I can easily skip timings to debug quicker (by setting t and ts to 0)
ship_accsess_able = False
# lists and hashes
# ----------------

crafting_station = [
    {"item": "knife", "crafted": False, "craft_requirements": {"nickle": 3, "silver": 2},
     "can craft": False},#knife info index 0
    
    {"item": "blast charge", "crafted": False, "craft_requirements": {"sulphur": 4, "boomstone": 2},
     "can craft": False},#blast charg infe index 1
    
    {"item": "laser cutter", "crafted": False, "craft_requirements": {"boomstone": 1, "silver": 2,
    "lumenstone": 5}, "can craft": False},#laser cutter info index 2
    
    {"item": "bio-flashlight", "crafted": False, "craft_requirements": {"lumenstone": 2, "silver": 2},
     "can craft": False},#bio flashlight info index 3
]


mineral_bag = {
    "nickle": 9,
    "silver": 9,
    "sulphur": 9,
    "boomstone": 9,
    "lumenstone": 9
}

# functions
# ---------
def restart(restart_time_in_seconds):# restarts all variable to starting values and re-runs from begining
    print("restarting...")
    for i in range(0, restart_time_in_seconds):# restart timer
        print(restart_time_in_seconds - i)
        time.sleep(ts)
        
    for crafting_station_reset in crafting_station:# restets crafting
        crafting_station_reset["crafted"] = False
        crafting_station_reset["can craft"] = False
        
    for mineral_bag_item, mineral_bag_quantity in mineral_bag.items():# resets minerals to 0
        mineral_bag[mineral_bag_item] = 0
    start_menu()


def start_menu():  # starting menu
    start_menu_loop = True
    print("""
-------------------------------------
Welcome to subnautica below graphics!
-------------------------------------
How to play:
when an option show up you can press the corresponding
number in the square brackets ([]) next to that option

your goal is to get to the unknown cavern with the proper
tools to complete the game and cure your infection
you will need to craft tools be able to create more tools
untill ultimatly you can accsess the unknown cavern

""")


    while start_menu_loop:# option loop will be included for every option
        option = 0  # option variable within each function so it can be reused and just redefines itself
        print("[1] start game")
        print("[2] quit game")
        print("Select an option:")
        
        try:
            option = int(input())
            
        except ValueError: # check for wrong input
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")

            
            continue  # goes back to top of loop
        if option == 1:
            start_menu_loop = False
            start_sequence() #runs start of game
        
        elif option == 2: # quits
            quit()

        else:  # checks for number outside of options
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")


def start_sequence(): # intro to game
    start_sequence_loop1 = True
    start_sequence_loop2 = True
    fire_damage = 1  # when this hits 3 you failed and the game restarts
    print("loading...")
    for i in range(0, t):# count down to let user know their starting
        print(t - i)
        time.sleep(ts)
        
    print("consciousness flickers as you jolt awake in a small warm, very warm room")
    time.sleep(ts * 2)
    for i in range(0, t):
        print("*beep*")
        time.sleep(ts)
        
    print("an intense sound of crackling fills your ears as you head fills with panic")
    time.sleep(ts * 2)
    print('"fire detected in emergency pod please extinguish immediately"')
    time.sleep(ts * 2)
    print("you can see your mini med bay, crafting station, and one small side of the room is on fire")
    time.sleep(ts * 2)

    
    while start_sequence_loop1:
        time.sleep(ts * 1)
        print("the fire on the wall is preventing you from accessing the extinguisher so for water you go grab the...")
        time.sleep(ts * 3)
        print("[1] large trash can, [2] bucket, [9] restart game")
        try:
            option = int(input())
        except ValueError:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")
            continue

        
        if option == 1:
            print("""
you lower the trash can down through a hatch in the
bottom of your pod, once filled with water you attempt
to bring it up to the fire but its to heavy, the fire grows.
You grab the bucket, fill it up put out the fire on the wall preventing
acsess to the extinguisher.
You can accesses the fire extinguisher.
            """)
            time.sleep(ts * 4)
            fire_damage += 1
            start_sequence_loop1 = False

        
        elif option == 2:
            print("""
you lower the bucket down through a hatch in the
bottom of your pod, once filled with water you
pour it onto the fire putting it out
You can accesses the fire extinguisher.
            """)
            time.sleep(ts * 3)
            start_sequence_loop1 = False

        
        elif option == 9:
            start_sequence_loop1 = False
            restart(t)

        
        else:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")

            
    while start_sequence_loop2:
        print("you look twords the mini med bay and crafting station. Do you...")
        print("[1] use the fire extinguisher on them, [2] or use the water bucket, [9] retart game")
        try:
            option = int(input())
        except ValueError:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")
            continue


        if option == 1:
            print("you successfully put out all fires")
            start_sequence_loop2 = False

        
        elif option == 2: #if you get 2nd option wring checks if you got both wrong and restarts
                          #otherwise continue game
            print("the water fails to put out the fires")
            print("you see sparks fly as the fire grows")
            fire_damage += 1
            if fire_damage == 3:
                print("you failed to put out the fires twice")
                restart(t)
                start_sequence_loop2 = False


            else:
                print("""
the water fails too put out the fires
you see sparks fly as the fire grows
but you manage to get the fire extinguisher
in time and put the fire out
                """)
                start_sequence_loop2 = False

            
        elif option == 9:
            start_sequence_loop2 = False
            restart()

        else:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")
    time.sleep(ts * 2)
    print("you take a moment to calm and go take a look out the window or your emergency strand pod")
    time.sleep(ts * 2.456789)
    print("you find yourself in a gain ocean spanning for miles")
    time.sleep(ts * 1.5)
    print('you cheack your planet scanner it reads "unknown planet"')
    print("you decide to check the local map to see 4 major areas")
    time.sleep(ts * 1.5)
    print("the crashed star ship up north that brought you to this planet")
    time.sleep(ts * 1.5)
    print("heat vents to the east-high resource density")
    time.sleep(ts * 1.5)
    print("caves to the west-high resource density")
    time.sleep(ts * 1.5)
    print("cavern of unknown properties-south of the starting pod")
    time.sleep(ts * 1.5)

    print("""
you pick up your mineral bag and empty tool pack
and notice that your covered in an infection,
a voice cries out from the south saying they can help you if you save them
""")
    time.sleep(ts * 2.856789)
    start_pod()




# places accessible to player (in order of game progression):
def start_pod():  # starting place you land/begin
    pod_loop = True
    print("""
WELCOME TO YOUR EMERGANCY LIFE POD

life support systems: operational
utility functionality: online
atmosphere: sustainable
    """)
    while pod_loop:
        plan_travel_loop = True
        craft_loop = True
        print("""
what operation would you like to access:
[1] crafting station
[2] plan travel
[8] mineral bag
[9] restart game
""")
        try:    #what pod operation you acsses
            option = int(input()) 
        except ValueError:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")
            continue


        
        if option == 1:
            # crafting station
            while craft_loop:
                i = 1
                #establishes what youcan and cant craft:
                for craftable_item in crafting_station: #goes through each thing in crafting_station
                    num_req_met = 0 #resets for each item it start to check
                    for mineral_req, quantity_req in craftable_item["craft_requirements"].items(): #goes therough the craft requiments in craftable_item
                        if mineral_bag[mineral_req] >= quantity_req: #compares the cost of the item to the amount in mineral bag
                            num_req_met += 1 #if we have enough, adds to this
                            if num_req_met == len(craftable_item["craft_requirements"]): #checks if all hte amount of requirments are met
                                craftable_item["can craft"] = True #allows you to craft if you have requirments
                            else:
                                craftable_item["can craft"] = False#stops you from crafting if you dont have the requirements and it was previously craftable
                                
                print("")
                print("your mineral bag:")
                for bag_mineral, amount in mineral_bag.items():#prints minerals owned
                    print(f"{bag_mineral}: {amount}")
                    
                print("")
                print("")
                print("avalible tools for crafting:")
                for tool in crafting_station: #prints tools in crafting station and what number to select
                    print(f"[{i}] {tool['item']}, crafting requirements: {tool['craft_requirements']}, crafted: {tool['crafted']}")
                    print("")
                    i += 1
                    
                print("[0] go back")
                print("[9] restart")
                print("what would you like to craft?")
                print("")
                try:                    
                    option = int(input())  #user inputs what item they want to craft
                except ValueError:
                    print(crafting_station)
                    print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")
                continue


                if 0 < option < len(crafting_station) + 1: #checks if the option input exsists in the inputs
                    if crafting_station[option - 1]["can craft"]:   #checks which if the item is craftble
                        if not crafting_station[option - 1]["crafted"]: #checks if item is already crafted
                            crafting_station[option - 1]["crafted"] = True
                            print("item crafted") 
                            for which_mineral, remove_amount in crafting_station[option - 1]["craft_requirements"].items(): #goes through the items craft requiments
                                for which_mineral_in_bag, amount_in_bag in mineral_bag.items():#goes through each mineral in mineral bag
                                    if which_mineral == which_mineral_in_bag: #checks if the mineral lines up which the craft requierment mineral
                                        amount_in_bag = amount_in_bag - remove_amount #sets new value for the amount of a mineral you have in the bag
                                        mineral_bag[which_mineral_in_bag] = amount_in_bag #sends that value to the mineral bag dict
                        elif crafting_station[option - 1]["crafted"]: #tells user you have already crafted this
                            print("you have already crafted this")
                    elif not crafting_station[option - 1]["can craft"]: #tells user they dont have the required minerals to craft this
                        print("you dont have the required minerals to craft this")
                elif option == 0:
                    craft_loop = False
                
                elif option == 9:
                    craft_loop = False
                    pod_loop = False
                    restart(t)
                
                else:       #tells user they did not select an item
                    print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")
#-----------------------------------------------------------------------------------------------


#plan travel:                    

        elif option == 2:
            option = 0
            while plan_travel_loop:
                print("""
where would you like to go:
[1] caves-west
[2] heat_vents-east
[3] crashed star ship-north
[4] cavern of unknown properties-south
[8] mineral bag
[9] restart game
[0] go back
""")
                 
                try:
                    option = int(input())
                    
                except ValueError:
                    print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")
                    continue
                
                if option == 1:
                    plan_travel_loop = False
                    pod_loop = False
                    travel_sequence(1)

                elif option == 2:
                    plan_travel_loop = False
                    pod_loop = False
                    travel_sequence(2)

                elif option == 3:
                    plan_travel_loop = False
                    pod_loop = False
                    travel_sequence(3)
                    
                elif option == 4:
                    plan_travel_loop = False
                    pod_loop = False
                    travel_sequence(4)
                    
                elif option == 8:
                    for bag_mineral, amount in mineral_bag.items():
                        print(f"{bag_mineral}: {amount}")
                        
                elif option == 9:
                    restart(t)
                    pod_loop = False
                    plan_travel_loop = False
                    
                elif option == 0:
                    plan_travel_loop = False
                
                else:
                    print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")
#--------------------------------------------------------------------
            
        elif option == 8:   #mineral_bag print
            print("Your mineral bag:")
            for bag_mineral, amount in mineral_bag.items():
                print(f"{bag_mineral}: {amount}")
                    # for bag_mineral, amount in mineral_bag.items loops through every item in mineral bag assining the bag_mineral, amount values
                    # f is used to format the print, everything within the curly brackets is code
                    # {bag_mineral} prints the mineral {amount} prints the amount of that mineral
                
        elif option == 9:
            restart(3)
            plan_travel_loop = False
            pod_loop = False

        
        else:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")

def travel_sequence(place):
    print("traveling")
    for i in range(0, t):
        print(t - i)
        time.sleep(ts)
    if place == 1:
        caves_west()
        
    elif place == 2:
        heat_vents_east()

    elif place == 3:
        crashed_ship_north(1)

    elif place == 4:
        ghost_river_south()
    

def caves_west():  # caves west of starting pod--------------------------------
    caves_loop = True
    print("""
you arrive at calm looking area with some small tunnles just bearly able to swim into
you notice alot of these area have litte shiny substences in them
""")
    time.sleep(ts * 1.5)
    while caves_loop:
        print("""
you go up to a tunnel upon close inspection you see a suspicious rock in the tunnel
[1] harvest it
[2] go back to pod
[8] mineral bag
[9] restart game
""")
        try:
            option = int(input())
                    
        except ValueError:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")
            continue
        if option == 1:
            harvest = random.randint(1, 3)
            if harvest == 1:
                mineral_bag["nickle"]+=1
                print("you got some nickel")
            elif harvest == 2:
                mineral_bag["silver"]+=1
                print("you got some silver")
            elif harvest == 3:
                print("you got nothing")
            continue

            
        elif option == 2:
            print("reterning")
            for i in range(0, t):
                print(t - i)
                time.sleep(ts)
            caves_loop = False
            start_pod()
            
        elif option == 8:
                for bag_mineral, amount in mineral_bag.items():
                    print(f"{bag_mineral}: {amount}")
                continue
                        
        elif option == 9:
            caves_loop = False
            restart(t)
        
        
        else:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")



def heat_vents_east():  # vents east of starting pod--------------------------------
    heat_vents_loop = True
    print("you arrive at area with very warm water, you can see some small red hot rocks near the heat vent")
    time.sleep(ts * 1.5)
    while heat_vents_loop:
        print("""
you go up to a heat vent and upon close inspection you see a the hot rock need a tool to pry it open
[1] harvest it
[2] go back to pod
[8] mineral bag
[9] restart game
""")
        try:
            option = int(input())
                    
        except ValueError:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")
            continue
        if option == 1:
            if crafting_station[0]["crafted"]:
                harvest = random.randint(1, 3)
                if harvest == 1:
                    mineral_bag["sulphur"]+=1
                    print("you got some sulphur")
                elif harvest == 2:
                    mineral_bag["boomstone"]+=1
                    print("you got some boomstone")
                elif harvest == 3:
                    print("you got nothing")
            else:
                print("you require a knife to open this")
            continue

            
        elif option == 2:
            print("reterning")
            for i in range(0, t):
                print(t - i)
                time.sleep(ts)
            heat_vents_loop = False
            start_pod()
            
        elif option == 8:
                for bag_mineral, amount in mineral_bag.items():
                    print(f"{bag_mineral}: {amount}")
                continue
                        
        elif option == 9:
            heat_vents_loop = False
            restart(t)
        
        else:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")


def crashed_ship_north(x):  # crashed ship north of starting pod--------------------------------
    global ship_accsess_able
    ship_loop = True
    
    if x == 1:
        print("you swim up to the large metal ship")
        time.sleep(ts * 1.5)
    elif x == 2:
        pass
    if not ship_accsess_able:
        print("you swim to the ship's only doors,")
        print("these doors are broken and too heavy to slide open")
        time.sleep(ts * 1.5)
        if not crafting_station[1]["crafted"]:
            print("you will need to craft a blast charge to open them")
            print("you swim back to your ship")
            time.sleep(ts*2)
            start_pod()
        elif crafting_station[1]["crafted"]:
            print("you use your blast charge to blow open the doors")
            ship_accsess_able = True
            crashed_ship_north(2)
    elif ship_accsess_able:
        print("you swim into the ship")
    #in the ship
    print("as you go into the ship you dim headlight flickers on,")
    time.sleep(ts * 1.5)
    while ship_loop:
        print("""
you take a look around and see a bright glowing substance
stuck to the walls
[1] harvest it
[2] go back to pod
[8] mineral bag
[9] restart game
""")
        try:
            option = int(input())
                    
        except ValueError:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")
            continue
        if option == 1:
            harvest = random.randint(1, 2)
            if harvest == 1:
                mineral_bag["lumenstone"]+=1
                print("you got some lumenstone")
            elif harvest == 2:
                print("the glow dissapears after you grab it")
                print("you got nothing")

            
        elif option == 2:
            print("reterning")
            for i in range(0, t):
                print(t - i)
                time.sleep(ts)
            ship_loop = False
            start_pod()
            
        elif option == 8:
                for bag_mineral, amount in mineral_bag.items():
                    print(f"{bag_mineral}: {amount}")
                continue
                        
        elif option == 9:
            ship_loop = False
            restart(t)
            break
        
        else:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")

    

def ghost_river_south():  # "cavern of unknown properties" later to be found as ghost river south of starting pod--------------------------------
    print("you swim down into a large carven")
    time.sleep(ts * 1.5)
    if not crafting_station[3]["crafted"]:
        print("its far too dark to see anything")
        print("you proceed to swim back to pod")
        time.sleep(ts * 1.5)
        start_pod()
    elif crafting_station[3]["crafted"]:
        print("""
you turn on your bio flashlight to reveal
a stunning image of a long grey sea,
filled with all kinds of unique wonderful fish
from the corner of your ear you hear a faint cry for help
somehow in english...
you look around too see a high tech vault infront of where the sound can from
""")
        time.sleep(ts * 5)
        if not crafting_station[2]["crafted"]:
            print("you do not have the required tools to prceed")
            print("you proceed to swim back to pod")
            time.sleep(ts * 1.5)
            start_pod()
        if crafting_station[2]["crafted"]:
            print("""
with a sense of ergency you open the vault with your laser cutter and proceed through,
as you swim through you hear a loud slam as the exit behind you becomes covered in rock
""")
            time.sleep(ts * 2.5)
            glowing_cavern()

def glowing_cavern():  # south-east from start point, only accessible from ghost river--------------------------------
    glowing_cavern_loop = True
    print("""
you feel the infection on you desolve away with the mystical water around you
you remove your oxygen mask to feel yourself breathing the water arounf you like air
any feeling of hunger is removed, your trapped in the most butifle cave,
the most wonderful thing you've ever seen, till the end of time... unaging
""")
    time.sleep(ts * 4.5)
    while glowing_cavern_loop:
        print("""
------------------------------------------
END OF SUBNAUTICA BELOW GRAPHICS
------------------------------------------
[1] restart
[2] quit
""")
        try:
            option = int(input())
                    
        except ValueError:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")
        if option == 1:
            glowing_cavern_loop = False
            restart(t)

        elif option == 2:
            glowing_cavern_loop = False
            quit()

        else:
             print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")
    


# main routine
# ------------
start_menu()
