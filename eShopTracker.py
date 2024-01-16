from nintendeals import noa, noe, noj
from commands import (printallregions, listallregions, welcome, region, listcommands, search, notifications, version)

#internetCheck = online.internetStatus()

#if internetCheck:
#    internet = "You are online"
#else:
#    internet = "You are offline, eShopTracker is working with limited functionality"


def overwriteFile(file):
    with open(file, 'w', encoding="utf-8") as f:
        clean = ""
        f.write(clean)
        f.close()


def runCommands(command):
    command = str.lower(command)
    if command == "printallregions":
        printallregions.printAllRegions()
    elif command == "listallregions":
        listallregions.listAllRegions()
    elif command == "welcome":
        welcome.welcomeMessage()
    elif command in ["region", "region -noa", "region -noe", "region -noj", "region -p -noa", "region -p -noe",
                     "region -p -noj"]:
        region.region(command)
    elif command == "search":
        search.search()
    elif command == "version":
        version.displayVersion()
    elif command == "commands":
        listcommands.commands()
    elif command == "commands -p":
        listcommands.detailedCommands()
    elif command == "version branch":
        version.displayVersionBranch()
    elif command == "version details":
        version.displayVersionDetails()
    else:
        print("Command Not Found")


def main():
    end = 0
    welcome.welcomeMessage()
    notifications.checkForUpdate()
    #print(internet)
    while end == 0:
        cmd = input("eShopTracker > ")
        runCommands(cmd)


main()

# for game in noa.list_switch_games():
#    if "Zelda" in game.title:
#        print(game.title)
#        print("NSUID: ", game.nsuid)
#        print("Release Date: ", game.release_date)
#        print("\n")


# for game in noa.search_switch_games(query="Zelda"):
#    print(game.title)
