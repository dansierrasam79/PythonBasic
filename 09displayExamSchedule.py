'''Write a Python program to display the examination schedule. (extract the date from
exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014'''

class displayExamSchedule:
    def __init__(self, examsched):
        self.exschd = examsched
    def displaySchedule(self):
        print("The examination will start from:", self.exschd[0], "/", self.exschd[1], "/",
        self.exschd[2])

#Driver code
if __name__ == "__main__":
    exam_st_dt = (11,12,2014)
    outputObject = displayExamSchedule(exam_st_dt)
    outputObject.displaySchedule()
