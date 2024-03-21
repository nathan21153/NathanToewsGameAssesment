#
#variables
#
import time
import random
choose_start_or_menu=0 #this is used to let phython know whether it should run start screen or ingame menu, this save lines of code (needs less functions)
c_or_s="start" #continue or start for what 
#
#lists and hashes
#

#
#functions
#
def main_menus (t, y): 
    print(continue_or_start)
    if t==0:
        print("----------------------------------")
        print("Welcome subnautica below graphics!")
        print("----------------------------------")
        print()
        choose_start_or_menu=1

    elif choose_start_or_menu==1:
        print("----------------------------------")
        print("Game paused")
        print()

    print("Select an option (input corresponding number):")
    print("Start, 1")
    print("Help, 2")
    print("")
#
#main routine
#
print()
start_screen_or_ingame_menu (choose_start_or_menu, gay)
