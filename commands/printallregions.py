from nintendeals import noa, noe, noj


def overwriteFile():
    with open('listAllRegions.txt', 'w', encoding="utf-8") as f:
        clean = ""
        f.write(clean)
        f.close()


def printAllRegions():
    overwriteFile()
    print("Printing all regions")
    for game in noa.list_switch_games():
        with open('listAllRegions.txt', 'a', encoding="utf-8") as f:
            Region = "Nintendo of America: "
            gameDetails = game.title
            f.write(Region + gameDetails + "\n")
            f.close()
    for game in noe.list_switch_games():
        with open('listAllRegions.txt', 'a', encoding="utf-8") as f:
            Region = "Nintendo of Europe: "
            gameDetails = game.title
            f.write(Region + gameDetails + "\n")
            f.close()
    for game in noj.list_switch_games():
        with open('listAllRegions.txt', 'a', encoding="utf-8") as f:
            Region = "Nintendo of Japan: "
            gameDetails = game.title
            f.write(Region + gameDetails + "\n")
            f.close()