import commands.region, commands.settings


def overwriteFile():
    with open('NintendoOfAmerica.txt', 'w', encoding="utf-8") as f:
        clean = ""
        f.write(clean)
        f.close()
    with open('NintendoOfEurope.txt', 'w', encoding="utf-8") as f:
        clean = ""
        f.write(clean)
        f.close()
    with open('NintendoOfJapan.txt', 'w', encoding="utf-8") as f:
        clean = ""
        f.write(clean)
        f.close()


def printAllRegions():
    if commands.settings.printallregions:
        overwriteFile()
        print("Printing all regions")
        commands.region.regionNA(1)
        commands.region.regionEU(1)
        commands.region.regionJP(1)
    else:
        print("This command is not enabled in settings")
