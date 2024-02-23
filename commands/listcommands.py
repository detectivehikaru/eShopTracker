import commands.settings


def regionCMDs():
    if commands.settings.listcommands:
        print("region -noa (displays all the software in US and Canada)")
        print("region -noe (displays all the software in Europe)")
        print("region -noj (displays all the software in Japan)")
        print("region -p -noa (displays all the software in US and Canada and prints them to a file)")
        print("region -p -noe (displays all the software in Europe and prints them to a file)")
        print("region -p -noj (displays all the software in Japan and prints them to a file)\n\n")
    else:
        print("This command is not enabled in settings")


def searchCommands():
    if commands.settings.listcommands:
        print("region -EU (searches for the specified software in Europe)")
        print("region -NA (searches for the specified software in US and Canada)")
        print("region -JP (searches for the specified software in Japan)")
        print("nsuid (searches for the nsuid and displays the software's detailed information)")
    else:
        print("This command is not enabled in settings")


def listBasicCommands():
    if commands.settings.listcommands:
        print("Listing all commands\n")
        print("listallregions - Lists all software from all regions\n")
        print("printallregions - Prints all software from all regions\n")
        print("region - Lists/Prints all software from a region\n")
        print("welcome - displays welcome message\n")
        print("version - displays program version\n")
        print("search - displays the list of software found from a search query\n")
        print("commands - displays all commands\n")
        print("commands -p (displays commands in detail)")
    else:
        print("This command is not enabled in settings")


def detailedCommands():
    if commands.settings.listcommands:
        print("Listing commands in detail\n\n")
        print("region")
        regionCMDs()
        print("search")
        searchCommands()
    else:
        print("This command is not enabled in settings")
