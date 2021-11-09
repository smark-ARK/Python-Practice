class Student:
    def __init__(self, name, roll, branch, year):
        self.name = name
        self.roll = roll
        self.branch = branch
        self.year = year

    def print_info(self):
        return 'Name:' + self.name+'Roll no.' + self.roll


stu1 = Student.print_info('SJ', '13')
print(stu1)
