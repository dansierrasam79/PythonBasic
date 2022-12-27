# Write a Python program to check if a number is positive, negative or zero.
if __name__ == "__main__":
    userInput = int(input("Enter any number: "))
    if userInput > 0:
        print(userInput, "is a positive number")
    elif userInput < 0:
        print(userInput, "is a negative number")
    else:
        print("Zero")
