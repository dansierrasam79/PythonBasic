#Write a Python program to concatenate all elements in a list into a string and return it.
class concatenateStringList:
    def __init__(self, myList):
        self.aList = myList
    def concatenateList (self):
        myString = ""
        for alphabet in self.aList:
            myString = myString + alphabet
        return myString
#Driver code
if __name__ == "__main__":
    aList = ["a", "b", "c", "d", "e"]
    outputObject = concatenateStringList(aList)
    print("The string is: ", outputObject.concatenateList())
