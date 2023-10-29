from nintendeals import noa, noe, noj


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


def NSUID_Search(nsuid):
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
        NSUID_Search(user_search)
    else:
        searchedItem(user_search)
