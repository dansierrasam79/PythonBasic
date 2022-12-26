'''Write a Python program to get the n (non-negative integer) copies of the first 2 characters of
a given string. Return the n copies of the whole string if the length is less than 2.'''
class returnStringCopies:
    def __init__(self, text, number):
        self.textStr = text
        self.n = number
    def returnStrCopies (self):
        if len (self.textStr) >= 2:
            return self.n*self.textStr[0:2]
        else:
            return self.n* self.textStr
#Driver code
if __name__ == "__main__":
    text = input ("Enter a string: ")
    nCopies = int (input("Enter number of copies: "))
    outputObject = returnStringCopies(text, nCopies)
    print(outputObject.returnStrCopies())
