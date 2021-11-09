class Person:
    def __init__(self, fname, lname, gender):
        self.fname = fname
        self.lname = lname
        self.gender = gender

    def printInfo(self):
        print('Name:', self.fname +
              ' '+self.lname, '\ngender:', self.gender)


person1 = Person('Abdul Rehman', 'Khan', 'M')
person1.printInfo()


class student(Person):
    def __init__(self, fname, lname, gender, branch):
        super().__init__(fname, lname, gender)
        self.branch = branch

    def printstu(self):
        print('Name:', self.fname +
              ' '+self.lname, '\ngender:', self.gender, '\nBranch:', self.branch)


student1 = student('Sumeria', 'Mahi', 'F', 'CSE')
student1.printstu()
