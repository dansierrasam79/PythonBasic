# Write a Python program to extract the filename from a given path.
if __name__ == "__main__":
    aFilePath = "/home/danielchakraborty/Desktop/comp.txt"
    for i in range(0,len(aFilePath)):
        if aFilePath[i] == "/":
            indxVal = i
    print(aFilePath[indxVal+1:])
