# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

class getIsString:
    def __init__(self, textString):
        self.givenString = textString
    def displayString (self):
        if self.givenString [0:2] == "Is":
            return self.givenString
        else:
            return "Is" + self.givenString
#Driver code
if __name__ == "__main__":
    givenString = input ("Enter a string: ")
    outputObject = getIsString(givenString)
    print(outputObject.displayString())
