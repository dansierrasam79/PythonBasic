#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

class numberDiff17:
    def __init__(self, number):
        self.n = number
    def testNumber (self):
        if self.n > 17:
            return self.n-17
        else:
            return abs(self.n-17)**2
#Driver code
if __name__ == "__main__":
    acceptedNumber = int(input ("Enter a number: "))
    outputObject = numberDiff17(acceptedNumber)
    print("Difference: ", outputObject.testNumber())
