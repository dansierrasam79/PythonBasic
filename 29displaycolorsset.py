'''Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}'''

class colorsinList:
    def __init__(self, colorlist1, colorlist2):
        self.color1 = colorlist1
        self.color2 = colorlist2
    def findColors(self):
        count = 0
        finalColorList = []
        for item1 in self.color1:
            for item2 in self.color2:
                if item1 != item2:
                    count = count + 1
                if count == 2:
                    finalColorList.append(item1)
                    count = 0
        return finalColorList
#Driver code
if __name__ == "__main__":
    color_list_1 = ["White", "Black", "Red"]
    color_list_2 = ["Red", "Green"]
    outputObject = colorsinList(color_list_1, color_list_2)
    print(outputObject.findColors())
