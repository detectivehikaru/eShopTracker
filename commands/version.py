version = "1.6.0"
version_message = "Version " + version
version_info = "version=" + version
version_control = "release"


def displayVersion():
    print(version_message)


def displayVersionBranch():
    print(version_control)


def displayVersionDetails():
    print(version_message + "-" + version_control)
