''' Write a Python program to find the operating system name, platform and platform release date.
Operating system name:
posix
Platform name:
Linux
Platform release:
4.4.0-47-generic'''

if __name__ == "__main__":
    import os, sys
    print("Operating system name: ", os.name)
    print("Platform name: ", sys.platform)
    print("Platform release: ", sys.version_info)
