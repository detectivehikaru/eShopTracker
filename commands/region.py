from nintendeals import noa, noe, noj
from colorama import Fore
import commands.listcommands


def regionNA(number):
    if number == 0:
        for game in noa.list_switch_games():
            Region = f"{Fore.WHITE}Nintendo of America: {Fore.GREEN}"
            gameDetails = ("{} {} / {}".format(Region, game.title, game.nsuid))
            print(gameDetails)
    if number == 1:
        for game in noa.list_switch_games():
            with open('NintendoOfAmerica.txt', 'a', encoding="utf-8") as f:
                Region = "Nintendo of America: "
                gameDetails = game.title
                f.write(Region + gameDetails + "\n")
                f.close()


def regionEU(number):
    if number == 0:
        for game in noe.list_switch_games():
            Region = f"{Fore.BLUE}Nintendo of Europe: {Fore.GREEN}"
            gameDetails = ("{} {} / {}".format(Region, game.title, game.nsuid))
            print(gameDetails)
    if number == 1:
        for game in noe.list_switch_games():
            with open('NintendoOfEurope.txt', 'a', encoding="utf-8") as f:
                Region = "Nintendo of Europe: "
                gameDetails = game.title
                f.write(Region + gameDetails + "\n")
                f.close()


def regionJP(number):
    if number == 0:
        for game in noj.list_switch_games():
            Region = f"{Fore.RED}Nintendo of Japan: {Fore.GREEN}"
            gameDetails = ("{} {} / {}".format(Region, game.title, game.nsuid))
            print(gameDetails)
    if number == 1:
        for game in noj.list_switch_games():
            with open('NintendoOfJapan.txt', 'a', encoding="utf-8") as f:
                Region = "Nintendo of Japan: "
                gameDetails = game.title
                f.write(Region + gameDetails + "\n")
                f.close()


def region(command):
    if command == "region":
        print("Invalid use of command region")
        print("Here's a list of region commands")
        commands.listcommands.regionCMDs()
    if command == "region -noa":
        regionNA(0)
    if command == "region -noe":
        regionEU(0)
    if command == "region -noj":
        regionJP(0)
    if command == "region -p -noa":
        regionNA(1)
    if command == "region -p -noe":
        regionEU(1)
    if command == "region -p -noj":
        regionJP(1)
