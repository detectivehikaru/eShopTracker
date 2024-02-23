import commands.region, commands.settings


def listAllRegions():
    if commands.settings.listallregions:
        print("List of games in NA")
        commands.region.regionNA(0)
        print("List of games in EU")
        commands.region.regionEU(0)
        print("List of games in JP")
        commands.region.regionJP(0)
    else:
        print("This command is not enabled in settings")
