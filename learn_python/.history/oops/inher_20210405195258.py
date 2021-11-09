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
    Person.__init__(self, fname, lname, gender)


student1 = student('Sumeria', 'Mahi', 'F')
student1.printInfo()
