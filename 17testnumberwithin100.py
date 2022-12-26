#Write a Python program to test whether a number is within 100 of 1000 or 2000.

class test100Within:
    def __init__(self, number):
        self.n = number
    def testNumber (self):
        if abs(1000 - self.n) < 100 or abs(2000-self.n) < 100:
            return True
        else:
            return False
#Driver code
if __name__ == "__main__":
    givenValue = int (input ("Enter a number: "))
    outputObject = test100Within(givenValue)
    if outputObject.testNumber() == True:
        print(givenValue, "is within 100 of 1000 or 2000")
    else:
        print(givenValue, " is NOT within 100 of 1000 or 2000")
