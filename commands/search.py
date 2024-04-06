from nintendeals import noa, noe, noj
from colorama import Fore
import commands.save, commands.settings, commands.info


def regionSearchItem(Item, Region):
    if Region == "NA":
        for game in noa.search_switch_games(query="{}".format(Item)):
            if Item in game.title:
                print(game.title, "/", game.nsuid, "NA")
    if Region == "EU":
        for game in noe.search_switch_games(query="{}".format(Item)):
            if Item in game.title:
                print(game.title, "/", game.nsuid, "EU")
    if Region == "JP":
        for game in noj.search_switch_games(query="{}".format(Item)):
            print(game.title, "/", game.nsuid, "JP")

    print(
        Fore.BLUE + "That is all the results for " + Fore.RED + Item + Fore.BLUE + " in the " + Region + " region" + Fore.GREEN)


def nsuidItem():
    if commands.settings.search:
        user_search = input("eShopTracker (Enter NSUID) > ")
        commands.info.nsuidSearch(user_search, commands.settings.saveAuto)
    else:
        print("This command is not enabled in settings")


def searchedItem(Item):
    for game in noa.search_switch_games(query="{}".format(Item)):
        if Item in game.title:
            print(game.title, "/", game.nsuid, "NA")
    for game in noe.search_switch_games(query="{}".format(Item)):
        if Item in game.title:
            print(game.title, "/", game.nsuid, "EU")
    for game in noj.search_switch_games(query="{}".format(Item)):
        print(game.title, "/", game.nsuid, "JP")

    print(Fore.BLUE + "That is all the results for " + Fore.RED + Item + Fore.GREEN)


def search():
    if commands.settings.search:
        user_search = input("eShopTracker (Search) > ")
        if user_search == "region -EU":
            user_search = input("eShopTracker (Search EU) > ")
            regionSearchItem(user_search, "EU")
        elif user_search == "region -NA":
            user_search = input("eShopTracker (Search NA) > ")
            regionSearchItem(user_search, "NA")
        elif user_search == "region -JP":
            user_search = input("eShopTracker (Search JP) > ")
            regionSearchItem(user_search, "JP")
        elif user_search == "nsuid":
            nsuidItem()
        else:
            searchedItem(user_search)
    else:
        print("This command is not enabled in settings")
