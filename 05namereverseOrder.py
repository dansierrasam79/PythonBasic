#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
class reversedString:
    def __init__(self, fullName):
        self.fName = fullName
    def reverString(self):
        reverseString = ""
        for i in range(len(self.fName)-1, -1,-1):
            reverseString = reverseString + self.fName[i]
        return reverseString

#Driver code
if __name__ == "__main__":
    fName = input ("Enter your full name: ")
    outputObject = reversedString(fName)
    print("Reversed string: ", outputObject.reverString())
