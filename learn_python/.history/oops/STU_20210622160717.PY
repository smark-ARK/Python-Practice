class Student:
    def __init__(self, name, roll, branch, year):
        self.name = name
        self.roll = roll
        self.branch = branch
        self.year = year

    def print_info(self):
        return 'Name:' + self.name+' '+'Rollno.' + self.roll+' '+self.branch+' '+self.year


stu1 = Student('SJ', '13', 'CSE', 'III')
print(stu1.print_info())
