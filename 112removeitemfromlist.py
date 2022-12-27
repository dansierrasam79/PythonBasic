# Write a Python program to remove the first item from a specified list.
if __name__ == "__main__":
    myList = [1,2,3,4,6,7,8,9,10]
    print("The items in the list are: ", myList)
    del myList[0]
    print("The items in the list after deletion is: ", myList)
