
crafting_station=[
    {"item":"knife", "crafted": False, "craft requirments": {"nickle": 3, "silver": 2}, "can craft":False, "choose_num":1},#knife info index 0
    {"item":"blast charge", "crafted": False, "craft requirments": {"sulphur": 4, "boomstone": 2}, "can craft":False, "choose_num":2},#blast charg infe index 1
    {"item":"laser cutter", "crafted": False, "craft requirments": {"boomstone": 1, "silver": 2, "lumenstone": 5}, "can craft":False, "choose_num":3},#laser cutter info index 2
    {"item":"bio-flashlight", "crafted": False, "craft requirments": {"lumenstone": 2, "silver": 2}, "can craft":False, "choose_num":4},#bio flashlight info index 3
]
mineral_bag={
    "nickle": 9,
    "silver": 9,
    "sulphur": 0,
    "boomstone": 0,
    "lumenstone": 0,
}
craftable_list=[
    
]
option = 1

if option == 1:
    #crafting station
    while True:
        print("""
what operation would you like to accses:
crafting station [1]
plan travel [2]
mineral bag [8]
restart game [9]
""")
        option=0
        i=1
        for craftable_item in crafting_station:
            num_req_met=0
            for mineral_req, quantity_req in craftable_item["craft requirments"].items():
                if mineral_bag[mineral_req] >= quantity_req:
                    num_req_met += 1
                    if num_req_met == len(craftable_item["craft requirments"]):
                        craftable_item["can craft"] = True
                        if not craftable_item in craftable_list:
                            craftable_list.append(craftable_item)
                    else:
                        craftable_item["can craft"] = False
                        if craftable_item in craftable_list:
                            craftable_list.remove(craftable_item)
            print("")
            print("your mineral bag:")
            for mineral, amount in mineral_bag.items():
                print(f"{mineral}: {amount}")
            print("")
            print("")
            print("avalible tools for crafting:")
            for tool in crafting_station:
                print(f"[{i}] {tool['item']}, crafting_requirments: {tool['craft requirments']}")
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
            if 0 < option <len(crafting_station):
                for item_choice_check in craftable_list:
                    if option == item_choice_check["choose_num"]:
                        for tools_replace in crafting_station:
                            if tools_replace["crafted"] == False:
                                if item_choice_check["choose_num"] == tools_replace["choose_num"]:
                                    print("item crafted")
                                    print("")
                                    item_choice_check["crafted"]=True
                                    tools_replace=item_choice_check        
                                    craftable_list.remove(item_choice_check)
                            else:
                                print("you have already crafted this")
                    else:
                        print("you cannot craft this")
                        continue
            elif option == 0:
                break
            elif option == 9:
                restart(t)
                break
            else:
                print("""
INPUT ERROR!! Please try again
type desierd option or input corresponding number:
""")
            #----------


