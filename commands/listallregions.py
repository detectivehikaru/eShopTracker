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
