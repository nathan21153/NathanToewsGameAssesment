#variables
#---------
import time
import random
s_or_p_menu=0 #this is used to let phython know whether it should run start or pause in the menus function, this save lines of code (needs less functions)
c_or_s=["start [1]", "continue [1]"] #continue or start for what ever menu your in

#lists and hashes
#----------------

#functions
#---------
def menus (): #pause and open screen menu
    global s_or_p_menu
    global c_or_s
    option=0 #option variable within each function so it can be reused and just redefines itself
    if s_or_p_menu == 0:
        s_or_p_menu+=1
        print("""
----------------------------------
Welcome subnautica below graphics!
----------------------------------
To select options in each menu:
input corresponding number
        """)
        print("start [1]")
    elif start_or_p_menu==1:
        print("-----------")
        print("Game paused")
        print("coninue [1]")
    print("Help [2]")
    print("quit game [3]")
    print("Select an option:")
    option=int(input())
    while True:
        if option == 1:
            begining()
        elif option == 2:
            print("""
Help:
------------------------------------------------------------
To select options in each menu:
input corresponding number type option you wish to choose
------------------------------------------------------------
continue? yes[1] quit [3]
            """)

            option=int(input())
        elif option == 3:
            quit
            
        else:
            print("""
MISS INPUT!! Please try again
type desierd option or input corresponding number:
            """)
            print(c_or_s[s_or_p_menu])
            print("Help [2]")
            print("quit game [3]")
            print("Select an option:")
            option=int(input())

def begining ():
    print ("placeholder")
    
#main routine
#------------
menus()
