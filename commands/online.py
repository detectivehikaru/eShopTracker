import requests
from colorama import Fore


def internetStatus():
    try:
        response = requests.get("https://google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False


def displayInternetStatus():
    if internetStatus():
        print("You are " + Fore.BLUE + "online" + Fore.GREEN)
    else:
        print("You are " + Fore.RED + "offline" + Fore.GREEN)
