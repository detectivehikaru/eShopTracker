from nintendeals import noa, noe, noj


def region(command):
    if command == "region":
        print("Invalid use of command region")
    if command == "region -noa":
        for game in noa.list_switch_games():
            print(game.title, "/", game.nsuid)
    if command == "region -noe":
        for game in noe.list_switch_games():
            print(game.title, "/", game.nsuid)
    if command == "region -noj":
        for game in noj.list_switch_games():
            print(game.title, "/", game.nsuid)
    if command == "region -p -noa":
        for game in noa.list_switch_games():
            with open('NintendoOfAmerica.txt', 'a', encoding="utf-8") as f:
                Region = "Nintendo of America: "
                gameDetails = game.title
                f.write(Region + gameDetails + "\n")
                f.close()
    if command == "region -p -noe":
        for game in noe.list_switch_games():
            with open('NintendoOfEurope.txt', 'a', encoding="utf-8") as f:
                Region = "Nintendo of Europe: "
                gameDetails = game.title
                f.write(Region + gameDetails + "\n")
                f.close()
    if command == "region -p -noj":
        for game in noj.list_switch_games():
            with open('NintendoOfJapan.txt', 'a', encoding="utf-8") as f:
                Region = "Nintendo of Japan: "
                gameDetails = game.title
                f.write(Region + gameDetails + "\n")
                f.close()
