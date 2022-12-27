# Write a Python program to convert height (in feet and inches) to centimeters.
if __name__ == "__main__":
    feet = input("Enter the height in feet: ")
    inches = input("Also add the inches: ")
    convertHeight = (int(feet) * 30.48) + (int(inches)*2.54)
    print("The height in centimeters is: ", convertHeight)
