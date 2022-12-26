#Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
class OSversion:
    def __init__(self):
        pass
    def OSBitMode(self):
        return sys.version[63:69]
#Driver code
if __name__ == "__main__":
    import sys
    outputObject = OSversion()
    print(outputObject.OSBitMode())
