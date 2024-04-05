#variables
#---------
import time
import random


#lists and hashes
#----------------

#---------------
#player items:
#tool pack

#mineral bag
#---------------

#functions
#---------
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
            if option == 1:
                begining()
                break
            elif option == 2:
                quit ()

        except ValueError:
            print("""
MISS INPUT!! Please try again
type desierd option or input corresponding number:
            """)
            continue #goes back to top of loop
            
        else: #checks for number outside of options
            print("""
MISS INPUT!! Please try again
type desierd option or input corresponding number:
            """)

def begining ():
    print("loading...")
    time.sleep(1)
    for i in range(1,6):
        x=6
        print(x-i)          
        time.sleep(1)#conut down to let user know their starting
    print("""
you wake up in a small space
*beep*
    """)

def start_pod (): #starting place you land
    print ("placeholder")
def crashed_ship_North (): #crashed ship north of starting pod
    print ("placeholder")
def caves_west (): #caves west of starting pod
    print ("placeholder")
def heat_vents_east (): #vents east of starting pod
    print ("placeholder")
def glowing_cavern (): #south-east from start ponit, only acsessable from ghost river
    print ("placeholder")


    
#main routine
#------------
start_menu()
