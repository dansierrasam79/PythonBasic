#Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

class threeNumbersSum:
    def __init__(self, gValue1, gValue2, gValue3):
        self.value1 = gValue1
        self.value2 = gValue2
        self.value3 = gValue3
    def numbersThreeSum(self):
        if self.value1 == self.value2 and self.value1 == self.value3:
            return (self.value1+ self.value2+ self.value3)*3
        else:
            return (self.value1+ self.value2+ self.value3)
#Driver code
if __name__ == "__main__":
    givenValue1 = int(input ("Enter a value: "))
    givenValue2 = int(input ("Enter a value: "))
    givenValue3 = int(input ("Enter a value: "))
    outputObject = threeNumbersSum(givenValue1, givenValue2, givenValue3)
    print(outputObject.numbersThreeSum())
