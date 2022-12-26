'''Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14'''

class displayDateTime:
    def __init__(self):
        pass
    def displayDateTime(self):
        print("The current date and time is: ", datetime.datetime.today())
        
#Driver code
if __name__ == "__main__":
    import datetime
    outputObject = displayDateTime()
    outputObject.displayDateTime()
