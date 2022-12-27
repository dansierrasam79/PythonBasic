#Write a Python program to filter the positive numbers from a list.
if __name__ == "__main__":
    myList = [0, 1, -2, -1, -4, 2, 3, -3, -5, 4, 5]
    myList2 = []
    for i in range(0, len(myList)):
        if myList[i] > 0:
            myList2.insert(i, myList[i])
    print(myList2)
