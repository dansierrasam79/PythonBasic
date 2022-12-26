#Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
class oddEvenCheck:
    def __init__(self, numOne):
        self.num1 = numOne
    def oddOrEven(self):
        if self.num1 % 2 == 0:
            return True
        else:
            return False
#Driver code
if __name__ == "__main__":
    userInput = int (input ("Enter number: "))
    outputObject = oddEvenCheck(userInput)
    if outputObject.oddOrEven()!= True:
        print ("Odd")
    else:
        print ("Even")
