from nintendeals import noa, noe, noj


def searchedItem(Item):
    for game in noa.search_switch_games(query="{}".format(Item)):
        print(game.title, "/", game.nsuid)
    for game in noe.search_switch_games(query="{}".format(Item)):
        print(game.title, "/", game.nsuid)
    #for game in noj.search_switch_games(query="{}".format(Item)):
    #    print(game.title, "/", game.nsuid)


def search():
    user_search = input("eShopTracker (Search) > ")
    searchedItem(user_search)
