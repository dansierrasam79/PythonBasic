# Write a Python program to calculate the hypotenuse of a right angled triangle.
if __name__ == "__main__":
    import math
    side = input("Enter the value of the first side: ")
    side2 = input("Enter the value of the second side: ")
    hypotenuse = math.pow(float(side) ** 2 + float(side2) ** 2, 0.5)
    print("The hypotenuse of the right-angled triangle is: ", hypotenuse)
