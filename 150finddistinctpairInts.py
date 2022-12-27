'''Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values.'''
def retoddPair(myList):
    finalList = []
    for i in range(0,len(myList)):
        for j in range(0, len(myList)):
            if i != j:
                product = myList[i]*myList[j]
                if product % 2 != 0:
                    tupleValues = (myList[i],myList[j])
                    finalList.append(tupleValues)
    return finalList
if __name__ == "__main__":
    aList = [1,2,3,4,5,6,7,8,9,10]
    print(retoddPair(aList))
