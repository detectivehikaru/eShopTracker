from art import text2art
from colorama import Fore
import commands.version, commands.settings


def welcomeMessage():
    if commands.settings.welcome:
        print(Fore.GREEN + "Welcome to eShop Tracker")
        eShopTracker_Art = text2art("eShopTracker")
        print(Fore.GREEN + eShopTracker_Art)
        print(Fore.BLUE + commands.version.version_message)
        print(Fore.GREEN + "To list all commands, type commands")
    else:
        pass
