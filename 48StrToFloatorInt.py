#Write a Python program to parse a string to Float or Integer.
class parseString:
    def __init__(self, givenString):
        self.myString = givenString
    def returnInteger(self):
        return int(self.myString)
    def returnFloat(self):
        return float(self.myString)
#Driver code
if __name__ == "__main__":
    gString = input("Enter a string: ")
    outputObject = parseString(gString)
    print("Integer:", outputObject.returnInteger())
    print("Float", outputObject.returnFloat())
