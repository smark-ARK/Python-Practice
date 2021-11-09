class company:
    companyName = "SMARK"

    def __init__(self, empName, empID, empSal):
        self.empName = empName
        self.empID = empID
        self.empSal = empSal

    def printInfo(self):
        print('The name of the company is:', self.companyName)

    def empInfo(self):
        print('Name:', self.empName, 'ID:', self.empID, 'Salary:', self.empSal)
