# Write a Python program to concatenate N strings.
if __name__ == "__main__":
    n = int(input("How many strings to do you want to concatenate: "))
    myString = ""
    for i in range(0, n):
        userInput = input("Enter a string: ")
        myString = myString + userInput
    print(myString)
