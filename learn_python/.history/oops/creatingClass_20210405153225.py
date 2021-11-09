class Employee:
    companyName = "SMARK"

    def __init__(self, empName, empID, empSal):
        self.empName = empName
        self.empID = empID
        self.empSal = empSal

    def printInfo(self):
        print('The name of the company is:', self.companyName)

    def empInfo(self):
        print('Name:', self.empName, '\n ID:',
              self.empID, '\n Salary:', self.empSal)


Employee1 = Employee('ARK', 160518733019, 120000)
Employee1.empInfo()
