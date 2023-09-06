from nintendeals import noa, noe, noj


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
    searchedItem(user_search)
