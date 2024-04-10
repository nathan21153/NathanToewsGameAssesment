# imports
# -------
import time
import random

# constants
# ---------
LUMENSTONE = "lumenstone"
BOOMSTONE = "boomstone"
SULPHUR = "sulphur"
CAN_CRAFT = "can craft"
SILVER = "silver"
NICKLE = "nickle"
CRAFT_REQUIREMENTS = "craft_requirements"
CRAFTED = "crafted"
ITEM = "item"
WEST = 1
EAST = 2
NORTH = 3
SOUTH = 4

# variables
# ---------
count_down_timer = 0  # used for timing on the countdowns
print_delay_time = 0  # (use variable as 1 for submission)used for timing on time.sleep, so I can easily skip timings to debug quicker (by setting t and ts to 0)
ship_accessible = False

# lists and hashes
# ----------------

crafting_station = [
    {ITEM: "knife", CRAFTED: False, CRAFT_REQUIREMENTS: {NICKLE: 3, SILVER: 2}, CAN_CRAFT: False},  # knife info index 0

    {ITEM: "blast_charge", CRAFTED: False, CRAFT_REQUIREMENTS: {SULPHUR: 4, BOOMSTONE: 2}, CAN_CRAFT: False},  # blast_charge info index 1

    {ITEM: "laser_cutter", CRAFTED: False, CRAFT_REQUIREMENTS: {BOOMSTONE: 1, SILVER: 2, LUMENSTONE: 5}, CAN_CRAFT: False},  # laser_cutter info index 2

    {ITEM: "bio_flashlight", CRAFTED: False, CRAFT_REQUIREMENTS: {LUMENSTONE: 2, SILVER: 2}, CAN_CRAFT: False},  # bio flashlight info index 3
]

mineral_bag = {
    NICKLE: 0,
    SILVER: 0,
    SULPHUR: 0,
    BOOMSTONE: 0,
    LUMENSTONE: 0
}


# functions
# ---------
def restart(restart_time_in_seconds):  # restarts all variable to starting values and re-runs from beginning
    global ship_accessible
    ship_accessible = False
    print("restarting...")
    for i in range(0, restart_time_in_seconds):  # restart timer
        print(restart_time_in_seconds - i)
        time.sleep(print_delay_time)

    for crafting_station_reset in crafting_station:  # restarts crafting
        crafting_station_reset[CRAFTED] = False
        crafting_station_reset[CAN_CRAFT] = False

    for mineral_bag_item, mineral_bag_quantity in mineral_bag.items():  # resets minerals to 0
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

you will need to craft tools be able to
get new materials to craft more tools
until ultimatly you can access the unknown cavern

""")

    while start_menu_loop:  # option loop will be included for every option
        print("[1] start game")
        print("[2] quit game")
        print("Select an option:")

        try:
            option = int(input())

        except ValueError:  # check for wrong input
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")

            continue  # goes back to top of loop
        if option == 1:
            start_menu_loop = False
            start_sequence()  # runs start of game

        elif option == 2:  # quits
            quit()

        else:  # checks for number outside of options
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")


def start_sequence():  # intro to game
    start_sequence_loop1 = True
    start_sequence_loop2 = True
    fire_damage = 1  # when this hits 3 you failed and the game restarts
    print("loading...")
    for i in range(0, count_down_timer):  # count down to let user know their starting
        print(count_down_timer - i)
        time.sleep(print_delay_time)  # waits amount of time

    print("consciousness flickers as you jolt awake in a small warm, very warm room")
    time.sleep(print_delay_time * 2)
    for i in range(0, count_down_timer):  # prints beep skips if t = 0
        print("*beep*")
        time.sleep(print_delay_time)

    print("an intense sound of crackling fills your ears as you head fills with panic")
    time.sleep(print_delay_time * 2)
    print('"fire detected in emergency pod please extinguish immediately"')
    time.sleep(print_delay_time * 2)
    print("you can see your mini med bay, crafting station, and one small side of the room is on fire")
    time.sleep(print_delay_time * 2)

    while start_sequence_loop1:
        time.sleep(print_delay_time * 1)
        print("the fire on the wall is preventing you from accessing the extinguisher so for water you go grab the...")
        time.sleep(print_delay_time * 3)
        print("""
[1] large trash can, [2] bucket
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
            print("""
you lower the trash can down through a hatch in the
bottom of your pod, once filled with water you attempt
to bring it up to the fire but its to heavy, the fire grows.
You grab the bucket, fill it up put out the fire on the wall preventing
access to the extinguisher.
You can accesses the fire extinguisher.
            """)
            time.sleep(print_delay_time * 4)
            fire_damage += 1
            start_sequence_loop1 = False

        elif option == 2:
            print("""
you lower the bucket down through a hatch in the
bottom of your pod, once filled with water you
pour it onto the fire putting it out
You can accesses the fire extinguisher.
            """)
            time.sleep(print_delay_time * 3)
            start_sequence_loop1 = False
        elif option == 9:
            start_sequence_loop1 = False
            restart(count_down_timer)
        else:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")

    while start_sequence_loop2:
        print("you look towords the mini med bay and crafting station. Do you...")
        print("""
[1] use the fire extinguisher on them, [2] or use the water bucket
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
            print("you successfully put out all fires")
            start_sequence_loop2 = False

        elif option == 2:  # if you get 2nd option wrong checks if you got both wrong and restarts
            # otherwise continue game
            print("the water fails to put out the fires")
            print("you see sparks fly as the fire grows")
            fire_damage += 1
            if fire_damage == 3:
                print("you failed to put out the fires twice")
                restart(count_down_timer)
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
            restart(count_down_timer)

        else:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")
    time.sleep(print_delay_time * 2)
    print("you take a moment to calm and go take a look out the window or your emergency strand pod")
    time.sleep(print_delay_time * 2.456789)
    print("you find yourself in a gain ocean spanning for miles")
    time.sleep(print_delay_time * 1.5)
    print('you check your planet scanner it reads "unknown planet"')
    print("you decide to check the local map to see 4 major areas")
    time.sleep(print_delay_time * 1.5)
    print("the crashed star ship up north that brought you to this planet")
    time.sleep(print_delay_time * 1.5)
    print("heat vents to the east-high resource density")
    time.sleep(print_delay_time * 1.5)
    print("caves to the west-high resource density")
    time.sleep(print_delay_time * 1.5)
    print("cavern of unknown properties-south of the starting pod")
    time.sleep(print_delay_time * 1.5)

    print("""
you pick up your mineral bag and empty tool pack
and notice that your covered in an infection,
a voice cries out from the south saying they can help you if you save them
""")
    time.sleep(print_delay_time * 2.856789)
    start_pod()


# places accessible to player (in order of game progression):
def start_pod():  # starting place you land/begin
    pod_loop = True
    print("""
WELCOME TO YOUR EMERGENCY LIFE POD

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
        try:  # what pod operation you accesses
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
                # establishes what you can and cant craft:
                for craft_able_item in crafting_station:  # goes through each thing in crafting_station
                    num_req_met = 0  # resets for each item it starts to check
                    for mineral_req, quantity_req in craft_able_item[CRAFT_REQUIREMENTS].items():  # goes through the craft requirements in craft_able_item
                        if mineral_bag[mineral_req] >= quantity_req:  # compares the cost of the items mineral requirements to the amount in mineral bag
                            # in mineral bag
                            num_req_met += 1  # if we have enough, adds to this
                            if num_req_met == len(craft_able_item[CRAFT_REQUIREMENTS]):  # checks if all the amount of requirements are met
                                craft_able_item[CAN_CRAFT] = True  # allows you to craft if you have requirements
                            else:
                                craft_able_item[CAN_CRAFT] = False  # stops you from crafting if you don't have the requirements
                                # and it was previously craft able

                print("")
                print("your mineral bag:")
                for bag_mineral, amount in mineral_bag.items():  # prints minerals owned
                    print(f"{bag_mineral}: {amount}")
                    # for bag_mineral, amount in mineral_bag.items loops through every item in mineral bag assigning the bag_mineral, amount values
                    # f is used to format the print, everything within the curly brackets is code
                    # {bag_mineral} prints the mineral {amount} prints the amount of that mineral

                print("")
                print("")
                print("available tools for crafting:")
                for tool in crafting_station:  # prints tools in crafting station and what number to select said tools
                    print(
                        f"[{i}] {tool[ITEM]}, crafting requirements: {tool['craft_requirements']}, crafted: {tool['crafted']}")
                    i += 1

                print("[0] go back")
                print("[9] restart")
                print("what would you like to craft?")
                print("")
                try:
                    option = int(input())  # user inputs what item they want to craft
                except ValueError:
                    print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")
                    continue

                if 0 < option < len(crafting_station) + 1:  # checks if the option input is a tool
                    if crafting_station[option - 1][CAN_CRAFT]:  # checks which is the item is craft able
                        if not crafting_station[option - 1][CRAFTED]:  # checks if item is already crafted
                            crafting_station[option - 1][CRAFTED] = True
                            print("item crafted")
                            for which_mineral, remove_amount in crafting_station[option - 1][CRAFT_REQUIREMENTS].items():  # goes through the items craft requirements
                                # .items() allows you to iterate through dicts assigning variable to the key, value, in this case (which_mineral, remove_amount)
                                for which_mineral_in_bag, amount_in_bag in mineral_bag.items():  # goes through each mineral in mineral bag
                                    if which_mineral == which_mineral_in_bag:  # checks if the mineral lines up which the craft requirement mineral
                                        amount_in_bag = amount_in_bag - remove_amount  # sets new value for the amount of a mineral you have in the bag
                                        mineral_bag[
                                            which_mineral_in_bag] = amount_in_bag  # sends that value to the mineral bag dict
                        elif crafting_station[option - 1][CRAFTED]:  # tells user you have already crafted this
                            print("you have already crafted this")
                    elif not crafting_station[option - 1][CAN_CRAFT]:  # tells user they don't have the required minerals to craft this
                        print("you dont have the required minerals to craft this")
                elif option == 0:
                    craft_loop = False

                elif option == 9:
                    craft_loop = False
                    pod_loop = False
                    restart(count_down_timer)

                else:  # tells user they did not select a valid option
                    print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")
        # -----------------------------------------------------------------------------------------------

        # plan travel:                    

        elif option == 2:
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
                    travel_sequence(1)  # sends value to travel sequence, so it know where to take you
                    # function used to reduce repeated code in options

                elif option == 2:
                    travel_sequence(2)

                elif option == 3:
                    travel_sequence(3)

                elif option == 4:
                    travel_sequence(4)

                elif option == 8:
                    for bag_mineral, amount in mineral_bag.items():
                        print(f"{bag_mineral}: {amount}")

                elif option == 9:
                    restart(count_down_timer)
                    pod_loop = False
                    plan_travel_loop = False

                elif option == 0:
                    plan_travel_loop = False

                else:
                    print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")
        # --------------------------------------------------------------------

        elif option == 8:  # mineral_bag print
            print("Your mineral bag:")
            for bag_mineral, amount in mineral_bag.items():
                print(f"{bag_mineral}: {amount}")

        elif option == 9:
            restart(3)
            pod_loop = False

        else:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")


def travel_sequence(place):
    print("traveling")
    for i in range(0, count_down_timer):
        print(count_down_timer - i)
        time.sleep(print_delay_time)

    if place == WEST:
        caves_west()
    elif place == EAST:
        heat_vents_east()
    elif place == NORTH:
        crashed_ship_north(1)
    elif place == SOUTH:
        ghost_river_south()


def caves_west():  # caves west of starting pod--------------------------------
    caves_loop = True
    print("""
you arrive at calm looking area with some small tunnels just barely able to swim into
you notice alot of these area have little shiny substences in them
""")
    time.sleep(print_delay_time * 1.5)
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
                mineral_bag[NICKLE] += 1
                print("you got some nickel")
            elif harvest == 2:
                mineral_bag[SILVER] += 1
                print("you got some silver")
            elif harvest == 3:
                print("you got nothing")
            continue

        elif option == 2:
            print("returning")
            for i in range(0, count_down_timer):
                print(count_down_timer - i)
                time.sleep(print_delay_time)
            caves_loop = False
            start_pod()

        elif option == 8:
            for bag_mineral, amount in mineral_bag.items():
                print(f"{bag_mineral}: {amount}")
            continue

        elif option == 9:
            caves_loop = False
            restart(count_down_timer)

        else:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")


def heat_vents_east():  # vents east of starting pod--------------------------------
    heat_vents_loop = True
    print("you arrive at area with very warm water, you can see some small red hot rocks near the heat vent")
    time.sleep(print_delay_time * 1.5)
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
            if crafting_station[0][CRAFTED]:
                harvest = random.randint(1, 3)
                if harvest == 1:
                    mineral_bag[SULPHUR] += 1
                    print("you got some sulphur")
                elif harvest == 2:
                    mineral_bag[BOOMSTONE] += 1
                    print("you got some boomstone")
                elif harvest == 3:
                    print("you got nothing")
            else:
                print("you require a knife to open this")
            continue

        elif option == 2:
            print("returning")
            for i in range(0, count_down_timer):
                print(count_down_timer - i)
                time.sleep(print_delay_time)
            heat_vents_loop = False
            start_pod()

        elif option == 8:
            for bag_mineral, amount in mineral_bag.items():
                print(f"{bag_mineral}: {amount}")
            continue

        elif option == 9:
            heat_vents_loop = False
            restart(count_down_timer)

        else:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")


def crashed_ship_north(x):  # crashed ship north of starting pod--------------------------------
    global ship_accessible
    ship_loop = True

    if x == 1:
        print("you swim up to the large metal ship")
        time.sleep(print_delay_time * 1.5)
    elif x == 2:
        pass
    if not ship_accessible:
        print("you swim to the ship's only doors,")
        print("these doors are broken and too heavy to slide open")
        time.sleep(print_delay_time * 1.5)
        if not crafting_station[1][CRAFTED]:
            print("you will need to craft a blast_charge to open them")
            print("you swim back to your ship")
            time.sleep(print_delay_time * 2)
            start_pod()
        elif crafting_station[1][CRAFTED]:
            print("you use your blast_charge to blow open the doors")
            ship_accessible = True
            crashed_ship_north(2)
    elif ship_accessible:
        print("you swim into the ship")
    # in the ship
    print("as you go into the ship you dim headlight flickers on,")
    time.sleep(print_delay_time * 1.5)
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
                mineral_bag[LUMENSTONE] += 1
                print("you got some lumenstone")
            elif harvest == 2:
                print("the glow dispersal after you grab it")
                print("you got nothing")

        elif option == 2:
            print("returning")
            for i in range(0, count_down_timer):
                print(count_down_timer - i)
                time.sleep(print_delay_time)
            ship_loop = False
            start_pod()

        elif option == 8:
            for bag_mineral, amount in mineral_bag.items():
                print(f"{bag_mineral}: {amount}")
            continue

        elif option == 9:
            restart(count_down_timer)
            break

        else:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")


def ghost_river_south():  # "cavern of unknown properties" later to be found as ghost river south of starting pod--------------------------------
    print("you swim down into a large cavern")
    time.sleep(print_delay_time * 1.5)
    if not crafting_station[3][CRAFTED]:
        print("its far too dark to see anything")
        print("you proceed to swim back to pod")
        time.sleep(print_delay_time * 1.5)
        start_pod()
    elif crafting_station[3][CRAFTED]:
        print("""
you turn on your bio flashlight to reveal
a stunning image of a long grey sea,
filled with all kinds of unique wonderful fish
from the corner of your ear you hear a faint cry for help
somehow in english...
you look around too see a high tech vault in front of where the sound can from
""")
        time.sleep(print_delay_time * 5)
        if not crafting_station[2][CRAFTED]:
            print("you do not have the required tools to proceed")
            print("you proceed to swim back to pod")
            time.sleep(print_delay_time * 1.5)
            start_pod()
        if crafting_station[2][CRAFTED]:
            print("""
you have a sense of urgency as you open the vault with your laser cutter and proceed through,
as you swim through you hear a loud slam as the exit behind you get covered in rock
""")
            time.sleep(print_delay_time * 2.5)
            glowing_cavern()


def glowing_cavern():  # south-east from start point, only accessible from ghost river--------------------------------
    glowing_cavern_loop = True
    print("""
you feel the infection on you resolve away with the mystical water around you
you remove your oxygen mask to feel yourself breathing the water around you like air
any feeling of hunger is removed, your trapped in the most beautiful cave,
the most wonderful thing you've ever seen, till the end of time... unaging
""")
    time.sleep(print_delay_time * 4.5)
    while glowing_cavern_loop:
        option = 0
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
            restart(count_down_timer)

        elif option == 2:
            quit()

        else:
            print("""
    INPUT ERROR!! Please try again
    type desired option or input corresponding number:
""")


# main routine
# ------------
start_menu()
