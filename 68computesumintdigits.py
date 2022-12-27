# Write a Python program to calculate the sum of the digits in an integer.
if __name__ == "__main__":
    print("We will find the sum of the digits of entered number")
    myString = input("Enter any number: ")
    total = 0
    for char in myString:
        total = total + int(char)
    print(total)
