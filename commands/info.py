import commands.save, commands.settings
from nintendeals import noa, noe, noj


def nsuidSave(title, product_code, unique_id, releaseDate, players, rating, region):
    saveInfo = []
    saveInfo.append(str(title))
    gameProductInfo = str(product_code) + str(unique_id)
    saveInfo.append(gameProductInfo)
    saveInfo.append(str(releaseDate))
    saveInfo.append(str(players))
    saveInfo.append(str(rating))
    saveInfo.append(str(region))
    commands.save.saveGameDetailsOntoFile(saveInfo)


def nsuidSearch(nsuid, saveOptions):
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

        if saveOptions == 0:
            user_input = input("Do you want to save this information (Y/N): ")

            if user_input == "Y":
                gameRating = str(game.rating[0]), str(game.rating[1])
                nsuidSave(game.title, game.product_code, game.unique_id, game.release_date, game.players, gameRating,
                          game.eshop.us_en)
        if saveOptions == 1:
            print("Auto saving")
            gameRating = str(game.rating[0]), str(game.rating[1])
            nsuidSave(game.title, game.product_code, game.unique_id, game.release_date, game.players, gameRating,
                      game.eshop.us_en)
        if saveOptions == 2:
            pass

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

        if saveOptions == 0:
            user_input = input("Do you want to save this information (Y/N): ")

            if user_input == "Y":
                gameRating = str(game.rating[0]), str(game.rating[1])
                nsuidSave(game.title, game.product_code, game.unique_id, game.release_date, game.players, gameRating,
                          game.eshop.uk_en)
        if saveOptions == 1:
            print("Auto saving")
            gameRating = str(game.rating[0]), str(game.rating[1])
            nsuidSave(game.title, game.product_code, game.unique_id, game.release_date, game.players, gameRating,
                      game.eshop.uk_en)
        if saveOptions == 2:
            pass

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

                    if saveOptions == 0:
                        user_input = input("Do you want to save this information (Y/N): ")

                        if user_input == "Y":
                            gameRating = str(game.rating[0]), str(game.rating[1])
                            nsuidSave(game.title, game.product_code, game.unique_id, game.release_date, game.players,
                                      gameRating,
                                      game.eshop.jp_jp)
                    if saveOptions == 1:
                        print("Auto saving")
                        gameRating = str(game.rating[0]), str(game.rating[1])
                        nsuidSave(game.title, game.product_code, game.unique_id, game.release_date, game.players,
                                  gameRating,
                                  game.eshop.jp_jp)
                    if saveOptions == 2:
                        pass
                    break

    except:
        regionCheck = regionCheck + 1

    if regionCheck == 3:
        print("The ID you entered was not found on any region")