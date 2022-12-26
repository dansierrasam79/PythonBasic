'''Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79'''
class computeInterest:
    def __init__(self, gPrincipal, gTime, gRate):
        self.principal = gPrincipal
        self.rate = gRate
        self.time = gTime
    def computeFutureValue(self):
        futureValue = self.principal + (self.principal*self.rate*self.time)/100
        return futureValue
#Driver code
if __name__ == "__main__":
    principal = 10000
    time = 7
    rate = 3.5
    outputObject = computeInterest(principal, time, rate)
    print(outputObject.computeFutureValue())
