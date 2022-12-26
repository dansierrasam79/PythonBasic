'''Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49'''
class equationSolution:
    def __init__(self, xValue, yValue):
        self.x = xValue
        self.y = yValue
    def displayEquation(self):
        return math.pow(self.x + self.y, 2)
# Driver code
if __name__ == "__main__":
    import math
    x = int(input("Enter the x-value: "))
    y = int(input("Enter the y-value: "))
    outputObject = equationSolution(x,y)
    print(outputObject.displayEquation())
