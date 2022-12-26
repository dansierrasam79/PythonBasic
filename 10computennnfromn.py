'''Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615'''
class computenValue:
    def __init__(self, n):
        self.number = n
    def computenVal(self):
        strVal2 = int(str(self.number)*2)
        strVal3 = int(str(self.number)*3)
        return self.number + strVal2 + strVal3
#Driver code
if __name__ == "__main__":
    givenValue = int(input("Please enter a number: "))
    outputObject = computenValue(givenValue)
    print(outputObject.computenVal())
