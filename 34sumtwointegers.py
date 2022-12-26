#Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
class twoIntegerTotal:
    def __init__(self, numOne, numTwo):
        self.num1 = numOne
        self.num2 = numTwo
    def computeSum(self):
        if self.num1 + self.num2 > 15 and self.num1 + self.num2 < 20:
            return 20
        else:
            return self.num1 + self.num2
# Driver code
if __name__ == "__main__":
    firstVal = int(input("Enter a value: "))
    secondVal = int(input("Enter a value: "))
    outputObject = twoIntegerTotal(firstVal, secondVal)
    print(outputObject.computeSum())
