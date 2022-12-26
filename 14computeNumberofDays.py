'''Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days'''

class computeDays:
    def __init__(self, date1, month1, year1, date2, month2, year2):
        self.d1 = date1
        self.m1 = month1
        self.y1 = year1
        self.d2 = date2
        self.m2 = month2
        self.y2 = year2
    def daysBetween(self):
        days1 = date(self.d1,self.m1, self.y1)
        days2 = date(self.d2, self.m2, self.y2)
        delta = days2 - days1
        return delta.days
# Driver code
if __name__ == "__main__":
    from datetime import date
    outputObject = computeDays(2014, 7, 2, 2022, 7, 11)
    print(outputObject.daysBetween())
