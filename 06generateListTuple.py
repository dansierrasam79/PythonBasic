'''Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')'''

class generateListTuple:
    def __init__(self, sequence):
        self.seqvalues = sequence
    def generateList(self):
        seqList = list(self.seqvalues.split())
        return seqList
    def generateTuple(self):
        seqTuple = tuple(self.seqvalues.split())
        return seqTuple
#Driver code
if __name__ == "__main__":
    sequenceValues = input("Enter comma separated values: ")
    outputObject = generateListTuple(sequenceValues)
    print(outputObject.generateList())
    print(outputObject.generateTuple())
