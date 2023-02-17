from nintendeals import noa, noe, noj
from commands import printallregions


def listAllRegions():
    print("List of games in NOA")
    for game in noa.list_switch_games():
        print(game.title, "/", game.nsuid)
    print("List of games in NOE")
    for game in noe.list_switch_games():
        print(game.title, "/", game.nsuid)
    print("List of games in NOJ")
    for game in noj.list_switch_games():
        print(game.title, "/", game.nsuid)


def overwriteFile():
    with open('listAllRegions.txt', 'w', encoding="utf-8") as f:
        clean = ""
        f.write(clean)
        f.close()


def runCommands(command):
    command = str.lower(command)
    if command == "printallregions":
        printallregions.printAllRegions()
    else:
        print("Command Not Found")


def main():
    end = 0
    print("Welcome to eShop Tracker")
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


#overwriteFile()

# for game in noa.search_switch_games(query="Zelda"):
#    print(game.title)
