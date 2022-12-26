#Write a Python program to get a string which is n (non-negative integer) copies of a given string.

class stringCopies:
    def __init__(self, givenStr, numberCopies):
        self.givenString = givenStr
        self.n = numberCopies
    def displayStringCopies(self):
        return self.n*self.givenString
#Driver code
if __name__ == "__main__":
    givenString = input("Enter a string: ")
    nCopies = int (input("Enter number of copies: "))
    outputObject = stringCopies (givenString, nCopies)
    print(outputObject.displayStringCopies())
