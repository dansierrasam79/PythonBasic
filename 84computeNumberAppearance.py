# Write a Python program to count the number occurrence of a specific character in a string.
if __name__ == "__main__":
    userInput = input("Enter a word or sentence: ")
    userInput2 = input("Enter a character: ")
    c = 0
    for i in range(0, len(userInput)):
        if userInput[i] == userInput2:
            c = c + 1
    print("The number of occurences of", userInput[i], "is ", c)
