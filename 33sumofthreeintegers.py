#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
class threeIntegerTotal:
    def __init__(self, oneValue, twoValue, threeValue):
        self.value1 = oneValue
        self.value2 = twoValue
        self.value3 = threeValue
    def areTwoEqual(self):
        if self.value1 == self.value2 or self.value1 == self.value3:
            return 0
        else:
            return self.value1 + self.value2 + self.value3
# Driver code
if __name__ == "__main__":
    value1 = int(input("Enter a value: "))
    value2 = int(input("Enter a value: "))
    value3 = int(input("Enter a value: "))
    outputObject = threeIntegerTotal(value1, value2, value3)
    print(outputObject.areTwoEqual())
