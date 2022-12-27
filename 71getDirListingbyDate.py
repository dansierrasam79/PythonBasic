# Write a Python program to get a directory listing, sorted by creation date.
#Lists all files in a directory
import os, time
dateList = []
c = 0
for file in os.listdir(r"C:\Users\Programming\Desktop"):
    if file.endswith(".txt"):
        pathFile = os.path.join(r"C:\Users\Programming\Desktop", file)
        creation = os.path.getctime(pathFile)
        dateList.insert(c, (file, creation, time.ctime(creation)))
        c = c + 1
        print(c)
#Sorting the date time but not using the conventional format
def second(elem):
    return elem[1]
dateList.sort(key=second)
#Console output of sorted dateList
for i in range(0, len(dateList)):
    print(dateList[i])
    print(len(dateList))
