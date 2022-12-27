#69. Write a Python program to sort three integers without using conditional statements andloops.
if __name__ == "__main__":
    myList = []
    n = int(input("How many items do you want to add to the list?: "))
    #Adding the items to the list
    for i in range(0, n, 1):
        userInput = int(input("Enter any integer: "))
        myList.insert(i, userInput)
    # Sort in ascending order
    myList.sort()
    print("Now let us display the integers in ascending order")
    #Displays the integers in ascending order
    print(myList)
    # Sort in ascending order
    myList.sort(reverse=True)
    #Displays the integers in descending order
    print("Now let us display the integers in descending order")
    print(myList)
