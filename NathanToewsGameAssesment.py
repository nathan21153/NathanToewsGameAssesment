#variables
#---------
import time
import random


#lists and hashes
#----------------

#functions
#---------
def start_menu (): #pause and open screen menu
    print ("""
-------------------------------------
Welcome to subnautica below graphics!
-------------------------------------
How to play:
when an option show up you can press thecorresponding
number in the square brackets ([]) next to that option
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
    print("placeholder")
    
#main routine
#------------
start_menu()
