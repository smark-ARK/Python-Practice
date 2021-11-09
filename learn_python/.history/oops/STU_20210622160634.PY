class Student:
    def __init__(self, name, roll, branch, year):
        self.name = name
        self.roll = roll
        self.branch = branch
        self.year = year

    def print_info(self):
        return 'Name:' + self.name+' '+'Roll no.' + self.roll


stu1 = Student('SJ', '13', 'CSE', 'III')
print(stu1.print_info())
