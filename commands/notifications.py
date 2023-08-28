import urllib.request
import commands.version

try:

    github_version_url = ("https://raw.githubusercontent.com/detectivehikaru/eShopTracker/main/githubResources/version" \
                         ".txt ")

    github_data = urllib.request.urlopen(github_version_url)

except:
    print("Unable to check for updates, ensure you have an active internet connection")


def checkForUpdate():
    try:
        latest_version = ""
        for line in github_data:
            latest_version = line.decode('utf-8')

        if commands.version.version_info == latest_version:
            print("You are up to date!")
        else:
            print(
                "eShopTracker has an update! Go to https://github.com/detectivehikaru/eShopTracker/releases and download "
                "the latest version")

    except:
        pass
