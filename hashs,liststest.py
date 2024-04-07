crafting_station=[
    {"item":"knife", "status":"uncrafted", "craft requirments": {"nickle": 3, "silver": 2}, "can craft":False},#knife info index 0
    {"item":"blast charge", "status":"uncrafted", "craft requirments": {"sulphur": 4, "boomstone": 2}, "can craft":False},#blast charg infe index 1
    {"item":"laser cutter", "status":"unrepaired", "craft requirments": {"boomstone": 1, "silver": 2, "lumenstone": 5}, "can craft":False},#laser cutter info index 2
    {"item":"bio-flashlight", "status":"uncrafted", "craft requirments": {"lumenstone": 2, "silver": 2}, "can craft":False},#bio flashlight info index 3
]
mineral_bag={
    "nickle": 3,
    "silver": 2,
    "sulphur": 0,
    "boomstone": 0,
    "lumenstone": 0,
}

option = 1

if option == 1:
    #crafting station
    while True:
        for craftable_item in crafting_station:
            print(craftable_item["item"])
            num_req_met=0
            for mineral_req, quantity_req in craftable_item["craft requirments"].items():
                print(f"  {mineral_req}  {quantity_req}")
                if mineral_bag[mineral_req] >= quantity_req:
                    num_req_met += 1
                    if num_req_met == len(craftable_item["craft requirments"]):
                        print("  craftable")
                        craftable_item["can craft"] = True
                        print(craftable_item["can craft"])
                else:
                    print("  you don't have the required minerals to craft this")
                    craftable_item["can craft"] = False
                    break
                
        option=0
        print("your mineral bag:")
        for mineral in mineral_bag:
            print(f"{mineral[]}: {mineral['quantity']}")
        print("avalible tools for crafting:")
        for tool in crafting_station:
            print(f"{tool['item']}, {tool['status']}, requirment: {tool['craft requirments']}","[", i, "]",sep=(''))
            i+=1
        print("what would you like to craft?")
        try:
            option=int(input())
        except ValueError:
            print("""
INPUT ERROR!! Please try again
type desierd option or input corresponding number:
""")
            continue
    #----------

