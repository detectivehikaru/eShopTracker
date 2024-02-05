from nintendeals import noa, noe, noj
from colorama import Fore
import commands.save


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

    print(Fore.BLUE + "That is all the results for " + Fore.RED + Item + Fore.BLUE + " in the " + Region + " region" + Fore.GREEN)


def nsuidSearch(nsuid):
    saveInfo = []
    regionCheck = 0
    regionCheckComplete = 0
    try:
        game = noa.game_info(nsuid)
        print(game.title)
        print(game.product_code, game.unique_id)
        print(game.release_date)
        print(game.players)
        print(str(game.rating[0]), game.rating[1])
        print(game.eshop.us_en)
        user_input = input("Do you want to save this information (Y/N): ")

        if user_input == "Y":
            saveInfo.append(str(game.title))
            gameProductInfo = str(game.product_code) + str(game.unique_id)
            saveInfo.append(gameProductInfo)
            saveInfo.append(str(game.release_date))
            saveInfo.append(str(game.players))
            gameRating = str(game.rating[0]), str(game.rating[1])
            saveInfo.append(str(gameRating))
            saveInfo.append(str(game.eshop.us_en))
            commands.save.saveGameDetailsOntoFile(saveInfo)

        regionCheckComplete = 1
    except:
        regionCheck = regionCheck + 1

    try:
        game = noe.game_info(nsuid)
        print(game.title)
        print(game.product_code, game.unique_id)
        print(game.release_date)
        print(game.players)
        print(str(game.rating[0]), game.rating[1])
        print(game.eshop.uk_en)
        user_input = input("Do you want to save this information (Y/N): ")

        if user_input == "Y":
            saveInfo.append(str(game.title))
            gameProductInfo = str(game.product_code) + str(game.unique_id)
            saveInfo.append(gameProductInfo)
            saveInfo.append(str(game.release_date))
            saveInfo.append(str(game.players))
            gameRating = str(game.rating[0]), str(game.rating[1])
            saveInfo.append(str(gameRating))
            saveInfo.append(str(game.eshop.uk_en))
            commands.save.saveGameDetailsOntoFile(saveInfo)

        regionCheckComplete = 1
    except:
        regionCheck = regionCheck + 1

    try:
        if regionCheckComplete == 0:
            for game in noj.list_switch_games():
                if game.nsuid == nsuid:
                    print(game.title)
                    print(game.product_code, game.unique_id)
                    print(game.release_date)
                    print(game.players)
                    print(str(game.rating[0]), game.rating[1])
                    print(game.eshop.jp_jp)
                    user_input = input("Do you want to save this information (Y/N): ")

                    if user_input == "Y":
                        saveInfo.append(str(game.title))
                        gameProductInfo = str(game.product_code) + str(game.unique_id)
                        saveInfo.append(gameProductInfo)
                        saveInfo.append(str(game.release_date))
                        saveInfo.append(str(game.players))
                        gameRating = str(game.rating[0]), str(game.rating[1])
                        saveInfo.append(str(gameRating))
                        saveInfo.append(str(game.eshop.jp_jp))
                        commands.save.saveGameDetailsOntoFile(saveInfo)
                    break

    except:
        regionCheck = regionCheck + 1

    if regionCheck == 3:
        print("The ID you entered was not found on any region")


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
        user_search = input("eShopTracker (Enter NSUID) > ")
        nsuidSearch(user_search)
    else:
        searchedItem(user_search)
