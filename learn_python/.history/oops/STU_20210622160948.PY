class Student:
    def __init__(self, name, roll, branch, year):
        self.name = name
        self.roll = roll
        self.branch = branch
        self.year = year

    def print_info(self):
        return 'Name:' + self.name+'  \n'+'Rollno.' + self.roll+'  \n'+'Branch: '+self.branch+'  \n'+'Year: '+self.year


stu1 = Student('SJ', '13', 'CSE', 'III')
stu2 = Student('Mug', '28', 'IT', '-1')
print(stu1.print_info())
print(stu2.print_info())
