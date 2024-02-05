import commands.region


def listAllRegions():
    print("List of games in NA")
    commands.region.regionNA(0)
    print("List of games in EU")
    commands.region.regionEU(0)
    print("List of games in JP")
    commands.region.regionJP(0)
