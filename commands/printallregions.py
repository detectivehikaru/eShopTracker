import commands.region


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
    overwriteFile()
    print("Printing all regions")
    commands.region.regionNA(1)
    commands.region.regionEU(1)
    commands.region.regionJP(1)
