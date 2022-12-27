# Write a Python program to calculate midpoints of a line.
if __name__ == "__main__":
    print("We will calculate the midpoint of a line")
    x1 = int(input("Enter the first x-coordinate: "))
    y1 = int(input("Enter the first y-coordinate: "))
    x2 = int(input("Enter the second x-coordinate: "))
    y2 = int(input("Enter the second y-coordinate: "))
    x = (x1+x2)/2
    y = (y1+y2)/2
    print("The midpoint of the line is ", x , " and ", y)
