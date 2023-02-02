from nintendeals import noa, noe, noj


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


def printAllRegions():
    for game in noa.list_switch_games():
        with open('listAllRegions.txt', 'a', encoding="utf-8") as f:
            Region = "Nintendo of America: "
            Game_Details = game.title
            f.write(Region + Game_Details + "\n")
            f.close()
    for game in noe.list_switch_games():
        with open('listAllRegions.txt', 'a', encoding="utf-8") as f:
            Region = "Nintendo of Europe: "
            Game_Details = game.title
            f.write(Region + Game_Details + "\n")
            f.close()
    for game in noj.list_switch_games():
        with open('listAllRegions.txt', 'a', encoding="utf-8") as f:
            Region = "Nintendo of Japan: "
            Game_Details = game.title
            f.write(Region + Game_Details + "\n")
            f.close()


def overwriteFile():
    with open('listAllRegions.txt', 'w', encoding="utf-8") as f:
        clean = ""
        f.write(clean)
        f.close


# for game in noa.list_switch_games():
#    if "Zelda" in game.title:
#        print(game.title)
#        print("NSUID: ", game.nsuid)
#        print("Release Date: ", game.release_date)
#        print("\n")

printAllRegions()
#overwriteFile()

# for game in noa.search_switch_games(query="Zelda"):
#    print(game.title)
