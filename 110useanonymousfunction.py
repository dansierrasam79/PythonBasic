# Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.
if __name__ == "__main__":
    myList = [15, 30, 45, 19, 17, 60, 75, 90, 23, 29, 71,93]
    for i in range(0, len(myList)):
        fifteen = lambda userInput: myList[i] % userInput == 0
        myVar = fifteen(15)
    if myVar == True:
        print(myList[i])
