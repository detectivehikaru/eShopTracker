version = "1.9.0"
version_message = "Version " + version
version_info = "version=" + version
version_control = "alpha"


def displayVersion():
    print(version_message)


def displayVersionBranch():
    print(version_control)


def displayVersionDetails():
    print(version_message + "-" + version_control)
