#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
class returnIntegerTrue:
    def __init__(self, givenValue1, givenValue2):
        self.value1 = givenValue1
        self.value2 = givenValue2
    def returnTrue(self):
        if self.value1 == self.value2:
            return True
        elif self.value1 + self.value2 == 5:
            return True
        elif abs(self.value1-self.value2) == 5:
            return True
        else:
            return False
#Driver code
if __name__ == "__main__":
    gValue1 = int(input("Enter a value: "))
    gValue2 = int(input("Enter a value: "))
    outputObject = returnIntegerTrue(gValue1, gValue2)
    print(outputObject.returnTrue())
