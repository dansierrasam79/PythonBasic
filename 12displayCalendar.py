'''Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.'''

class displayMonthYear:
    def __init__(self, givenMonth, givenYear):
        self.month = givenMonth
        self.year = givenYear
    def displayMonthYear(self):
        return calendar.prmonth(self.year,self.month)
#Driver code
if __name__ == "__main__":
    import calendar
    inputMonth = int(input("Enter the month: "))
    inputYear = int(input("Enter the year: "))
    outputObject = displayMonthYear(inputMonth, inputYear)
    outputObject.displayMonthYear()
