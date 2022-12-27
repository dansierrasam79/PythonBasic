# Write a Python program to test whether all numbers of a list is greater than a certain number.
if __name__ == "__main__":
    myList = [1,2,3,4,5,6,7,8,9,10,13,15,16,19,29,37,53,77,91,103]
    userInput = int(input("Please enter the number that you would like to check against this list: "))
    c = 0
    for item in myList:
        if userInput >= item:
            c = c + 1
    if c == len(myList):
        print(userInput, " IS the greatest number against this list")
    else:
        print(userInput, " is NOT the greatest number against this list")
