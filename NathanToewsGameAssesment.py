#variables
#---------
import time
import random
#lists and hashes
#----------------
crafting_station=[
    {"item":"knife", "status":"uncrafted"},#index 0 craft requirments: 3 nickle, 2 silver
    {"item":"blast charge", "status":"uncrafted"},#index 1 craft requirments: 2 sulfer, 4 boomstone
    {"item":"laser cutter", "status":"unrepaired"},#index 2 craft requirments: 1 boomstone, 2 silver, 5 nickle
    {"item":"bio-flashlight", "status":"uncrafted"},#index 3 craft requirments: 2 lumenstone, 2 silver
    ]
mineral_bag=[
    {"mineral":"nickle", "quantity": 0},#index 0
    {"mineral":"silver", "quantity": 0},#index 1
    {"mineral":"sulfer", "quantity": 0},#index 2
    {"mineral":"boomstone", "quantity": 0},#index 3
    {"mineral":"lumen-stone", "quantity": 0},#index 4
    ]
#functions
#---------
def restart ():
    for i in range (1,4):
        x=4
        print(x-i)
        time.sleep(1)
    start_menu ()
def start_menu (): #pause and open screen menu
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
MISS INPUT!! Please try again
type desierd option or input corresponding number:
            """)
            continue #goes back to top of loop
        if option == 1:
            start_sequence()
            break
        elif option == 2:
                quit ()
        elif option == 9:
            restart()
            break
            
        else: #checks for number outside of options
            print("""
MISS INPUT!! Please try again
type desierd option or input corresponding number:
            """)

def start_sequence ():
    option=0
    fire_damage=1 #when this hits 3 you failed and the game restarts
    print("loading...")
    for i in range(1,6):
        x=6
        print(x-i)         
        time.sleep(1)#conut down to let user know their starting
    print("consiousness flickers as you jolt awake in a small warm, very warm room")
    time.sleep(2)
    for i in range (1, 4):
        print("*beep*")
        time.sleep(1)
    print("an intesnse sound of crackeling fills your ears as you head fills with panic")
    time.sleep (2)
    print('"fire detected in emergancy pod please extinguish immedietly"')
    time.sleep (2)
    print("you can see your mini med bay, crafting station, and one small side of the room is on fire")
    time.sleep (2)
    while True:
        time.sleep (1)
        print("the fire on the wall is perventing you from acsessing the extinisher so for water you go grab the...")
        time.sleep (3)
        print("large trash can [1], bucket [2]")
        try:
            option = int(input())
        except ValueError:
            print("""
MISS INPUT!! Please try again
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
            restart()
            break
        else:
            print("""
MISS INPUT!! Please try again
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
MISS INPUT!! Please try again
type desierd option or input corresponding number:
            """)
            continue
        
        if option == 1:
            print("you sucsesfully put out all fires")
            start_pod()
            break
        elif option == 2:
            print("the water fails to put out the fires")
            print("you see sparks fly as the fire grows")
            fire_damage+=1
            if fire_damage == 3:
                print("you failed to put out the fires twice")
                print("game restarting...")
                restart()
                break
        
            else:
                print("""
the water fails too put out the fires
you see sparks fly as the fire grows
but you manage to get the fire extingisher
in time and put the fire out
                """)
                start_pod()
                break
        elif option == 9:
            restart()
            break
            
        else:
            print("""
MISS INPUT!! Please try again
type desierd option or input corresponding number:
            """)
    time.sleep(1)
    print("you take a moment to calm and go take a look out the window or your emergency strand pod")
    time.sleep(2.456789)
    print("you find yourself in a gaint ocean spanning for miles")
    time.sleep(1.5)
    print('you cheack your planet scanner it reads "unkown planet"')
    print("you decide to check the local map to see 4 major areas")
    time.sleep(2.5)
    print("the crashed star ship up north that brought you to this planet")
    time.sleep(1.5)
    print("heat vents to the east-high resource density")
    time.sleep(1.5)
    print("caves to the west-high resource density")
    time.sleep(1.5)
    print("cavern of unknown proproties-south of the starting pod")

def start_pod (): #starting place you land
    print("")
def crashed_ship_North (): #crashed ship north of starting pod
    print("placeholder")
def caves_west (): #caves west of starting pod
    print("placeholder")
def heat_vents_east (): #vents east of starting pod
    print("placeholder")
def ghost_river_south (): #"cavern of unknown proproties" later to be found as ghost river south of starting pod
    print("placeholder")
def glowing_cavern (): #south-east from start ponit, only acsessable from ghost river
    print("placeholder")  
#main routine
#------------
start_menu()
