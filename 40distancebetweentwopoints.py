# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
class distanceCartesian:
    def __init__(self, gx1, gx2, gy1, gy2):
        self.x1 = gx1
        self.x2 = gx2
        self.y1 = gy1
        self.y2 = gy2
    def computeDistance(self):
        return (self.x2 - self.x1)/(self.y2-self.y1)
# Driver code
if __name__ == "__main__":
    x1 = int(input("Enter x1 value: "))
    x2 = int(input("Enter x2 value: "))
    y1 = int(input("Enter y1 value: "))
    y2 = int(input("Enter y2 value: "))
    outputObject = distanceCartesian(x1,x2,y1,y2)
    print("Cartesian Distance: ", outputObject.computeDistance())
