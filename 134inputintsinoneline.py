# Write a Python program to input two integers in a single line.
if __name__ == "__main__":
    myList = []
    userInput = input("Enter two values separated by a comma: ")
    myList = userInput.split(",")
    total = 0
    for item in myList:
        total = total + int(item)
    print("The total of the two entered values is: ", total)
