#imports
#-------
import time
import random
#variables
#---------
t=0 #used for timing on the countdowns
ts=0 #(use variable as 1 for submission)used for timing on time.sleep so I can easily skip timings to debug quicker (by setting t and ts to 0)
#lists and hashes
#----------------

crafting_station=[
    {"item":"knife", "crafted": False, "craft requirments": {"nickle": 3, "silver": 2}, "can craft":False},# "choose_num":1},#knife info index 0
    {"item":"blast charge", "crafted": False, "craft requirments": {"sulphur": 4, "boomstone": 2}, "can craft":False},# "choose_num":2},#blast charg infe index 1
    {"item":"laser cutter", "crafted": False, "craft requirments": {"boomstone": 1, "silver": 2, "lumenstone": 5}, "can craft":False},# "choose_num":3},#laser cutter info index 2
    {"item":"bio-flashlight", "crafted": False, "craft requirments": {"lumenstone": 2, "silver": 2}, "can craft":False}# "choose_num":4},#bio flashlight info index 3
]
mineral_bag={
    "nickle": 9,
    "silver": 9,
    "sulphur": 9,
    "boomstone": 9,
    "lumenstone": 9,
}

craftable_list=[
    
]
#functions
#---------
def restart(restart_time_in_seconds):
    print("restarting...")
    for i in range (0, restart_time_in_seconds):
        print(restart_time_in_seconds-i)
        time.sleep(ts)
    start_menu()
def start_menu(): #starting menu
    print ("""
-------------------------------------
Welcome to subnautica below graphics!
-------------------------------------
How to play:
when an option show up you can press the corresponding
number in the square brackets ([]) next to that option

you can enter 9 at any input point in the game to restart

    """)
    while True:
        option=0 #option variable within each function so it can be reused and just redefines itself
        print("start game [1]")
        print("quit game [2]")
        print("Select an option:")
        try:
            option=int(input())
        except ValueError:
            print("""
INPUT ERROR!! Please try again
type desierd option or input corresponding number:
            """)
            continue #goes back to top of loop
        if option == 1:
            start_sequence()
            break
        elif option == 2:
            quit()
        elif option == 9:
            restart(t)
            break
            
        else: #checks for number outside of options
            print("""
INPUT ERROR!! Please try again
type desierd option or input corresponding number:
            """)

def start_sequence():
    option=0
    fire_damage=1 #when this hits 3 you failed and the game restarts
    print("loading...")
    for i in range(0,t):
        print(t-i)         
        time.sleep(ts)#conut down to let user know their starting
    print("consiousness flickers as you jolt awake in a small warm, very warm room")
    time.sleep(ts*2)
    for i in range (0, t):
        print("*beep*")
        time.sleep(ts)
    print("an intesnse sound of crackeling fills your ears as you head fills with panic")
    time.sleep (ts*2)
    print('"fire detected in emergancy pod please extinguish immedietly"')
    time.sleep (ts*2)
    print("you can see your mini med bay, crafting station, and one small side of the room is on fire")
    time.sleep (ts*2)
    while True:
        time.sleep (ts*1)
        print("the fire on the wall is perventing you from acsessing the extinisher so for water you go grab the...")
        time.sleep (ts*3)
        print("large trash can [1], bucket [2]")
        try:
            option = int(input())
        except ValueError:
            print("""
INPUT ERROR!! Please try again
type desierd option or input corresponding number:
            """)
            continue
        if option == 1:
            print("""
you lower the trash can down through a hatch in the
bottom of your pod, once filled with water you attempt
to bring it up to the fire but its to heavy, the fire grows.
You grab the bucket, fill it up put out the fire on the wall perventing
acsess to the extinguisher.
You can acsses the fire extinusher.
            """)
            fire_damage+=1
            break
        elif option == 2:
            print("""
you lower the bucket down through a hatch in the
bottom of your pod, once filled with water you
pour it onto the fire putting it out
You can acsses the fire extinusher.
            """)
            break
        elif option == 9:
            restart(t)
            break
        else:
            print("""
INPUT ERROR!! Please try again
type desierd option or input corresponding number:
            """)
    while True:
        option = 0
        print("you look twords the mini med bay and crafting station. Do you...")
        print("use the fire extinguisher on them [1], or use the water bucket [2]")
        try:
            option = int(input())
        except ValueError:
            print("""
INPUT ERROR!! Please try again
type desierd option or input corresponding number:
            """)
            continue
        
        if option == 1:
            print("you sucsesfully put out all fires")
            break
        elif option == 2:
            print("the water fails to put out the fires")
            print("you see sparks fly as the fire grows")
            fire_damage+=1
            if fire_damage == 3:
                print("you failed to put out the fires twice")
                restart(t)
                break
        
            else:
                print("""
the water fails too put out the fires
you see sparks fly as the fire grows
but you manage to get the fire extingisher
in time and put the fire out
                """)
                break
        elif option == 9:
            restart()
            break
            
        else:
            print("""
INPUT ERROR!! Please try again
type desierd option or input corresponding number:
            """)
    time.sleep(ts*1)
    print("you take a moment to calm and go take a look out the window or your emergency strand pod")
    time.sleep(ts*2.456789)
    print("you find yourself in a gaint ocean spanning for miles")
    time.sleep(ts*1.5)
    print('you cheack your planet scanner it reads "unkown planet"')
    print("you decide to check the local map to see 4 major areas")
    time.sleep(ts*1.5)
    print("the crashed star ship up north that brought you to this planet")
    time.sleep(ts*1.5)
    print("heat vents to the east-high resource density")
    time.sleep(ts*1.5)
    print("caves to the west-high resource density")
    time.sleep(ts*1.5)
    print("cavern of unknown proproties-south of the starting pod")
    time.sleep(ts*1.5)
    print("you pick up your mineral bag and empty tool pack")
    print("your mineral bag can be accsessed at any time by pressing [8]")
    start_pod(1)



#places acssesable to player (in order of game porgression):
def start_pod(x): #starting place you land/begin
    print("""
life support systems: operational
utility functionallity: online
atmosphere: sustainable
    """)
    while True:
        option =0
        print("""
what operation would you like to accses:
crafting station [1]
plan travel [2]
mineral bag [8]
restart game [9]
""")
        try:
            option = int(input())
        except ValueError:
            print("""
INPUT ERROR!! Please try again
type desierd option or input corresponding number:
            """)
            continue
        if option == 1:
            craft_loop = True
            #crafting station
            while craft_loop:
                option=0
                i=1
                for craftable_item in crafting_station:
                    num_req_met=0
                    for mineral_req, quantity_req in craftable_item["craft requirments"].items():
                        if mineral_bag[mineral_req] >= quantity_req:
                            num_req_met += 1
                            if num_req_met == len(craftable_item["craft requirments"]):
                                craftable_item["can craft"] = True
                                # if not craftable_item in craftable_list:
                                #     craftable_list.append(craftable_item)
                            else:
                                craftable_item["can craft"] = False
                                # if craftable_item in craftable_list:
                                #     craftable_list.remove(craftable_item)
                print("")
                print("your mineral bag:")
                for mineral, amount in mineral_bag.items():
                    print(f"{mineral}: {amount}")
                print("")
                print("")
                print("avalible tools for crafting:")
                for tool in crafting_station:
                    print(f"[{i}] {tool['item']}, crafting requirments: {tool['craft requirments']}, crafted: {tool['crafted']}")
                    print("")
                    i+=1
                print("go back [0]")
                print("restart [9]")
                print("what would you like to craft?")
                print("")
                try:
                    option=int(input())
                except ValueError:
                    print("""
INPUT ERROR!! Please try again
type desierd option or input corresponding number:
""")
                    continue
                if 0 < option <len(crafting_station)+1:
                    if crafting_station[option-1]["can craft"]:
                        crafting_station[option-1]["crafted"]=True

                        for which_mineral, remove_amount in crafting_station[option-1]["craft requirments"].items():
                            for which_mineral_in_bag, amount_in_bag in mineral_bag.items():
                                if which_mineral == which_mineral_in_bag:
                                    amount_in_bag = amount_in_bag - remove_amount
                                    mineral_bag[which_mineral_in_bag] = amount_in_bag
                    # for item_choice_check in craftable_list:
                    #     if option == item_choice_check["choose_num"]:
                    #         for tools_replace in crafting_station:
                    #             if tools_replace["crafted"] == False:
                    #                 if item_choice_check["choose_num"] == tools_replace["choose_num"]:
                    #                     print("item crafted")
                    #                     print("")
                    #                     item_choice_check["crafted"]=True
                    #                     tools_replace=item_choice_check
                    #                     craftable_list.remove(item_choice_check)
                    #                     for which_mineral, remove_amount in tools_replace["craft requirments"].items():
                    #                         for which_mineral_in_bag, amount_in_bag in mineral_bag.items():
                    #                             if which_mineral == which_mineral_in_bag:
                    #                                 amount_in_bag = amount_in_bag - remove_amount
                    #                                 mineral_bag[which_mineral_in_bag] = amount_in_bag
                    #             else:
                    #                 print("you have already crafted this")
                    #     else:
                    #         print("you cannot craft this")
                    #         continue
                elif option == 0:
                    craft_loop = False
                elif option == 9:
                    restart(t)
                    break
                else:
                    print("""
INPUT ERROR!! Please try again
type desierd option or input corresponding number:
""")
                #----------

        elif option == 2:
            print("")
        elif option == 8:
            print("Your mineral bag:")
            for mineral, amount in mineral_bag.items():
                print(f"{mineral}: {amount}")
        elif option == 9:
            restart(3)
            break
        else:
            print("""
INPUT ERROR!! Please try again
type desierd option or input corresponding number:
        """)


def caves_west(): #caves west of starting pod
    #for mineral in mineral_bag loops through every index in mineral bag
    #f is used to format the print, everything within the curly brackets is code
    #{mineral[ loops each time with the following index starting from mineral_bag[0]
    #the index it print is mineral_bag[mineral] where mineral is just a number
    #'mineral' prints what value sored in mineral: in the mineral_bag hash in order of indexs, same with 'quantity'
    print("placeholder")
def heat_vents_east(): #vents east of starting pod
    print("placeholder")
def crashed_ship_North(): #crashed ship north of starting pod
    print("placeholder")
def ghost_river_south(): #"cavern of unknown proproties" later to be found as ghost river south of starting pod
    print("placeholder")
def glowing_cavern(): #south-east from start ponit, only acsessable from ghost river
    print("placeholder")
#main routine
#------------
start_menu()

while True:
    if option == 123:
        print()

    elif option == 8:
        for mineral in mineral_bag:
            print(f"{mineral['mineral']}: {mineral['quantity']}")
    elif option == 9:
        restart(t)
        break
    else:
        print("""
    INPUT ERROR!! Please try again
    type desierd option or input corresponding number:
    """)
