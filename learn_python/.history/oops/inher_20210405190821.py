class Person:
    def __init__(self, fname, lname, gender):
        self.fname = fname
        self.lname = lname
        self.gender = gender

    def printInfo(self):
        print('Name:', self.fname+self.lname, 'gender:', self.gender)
