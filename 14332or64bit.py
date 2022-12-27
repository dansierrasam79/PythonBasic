# Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on the operating system.
if __name__ == "__main__":
    import platform
    print(platform.architecture()[0])
