class Employee:
    def __init__(self, fname, lname, annsal):
        self.fname = fname
        self.lname = lname
        self._annsal = annsal

    def give_raise(self, rais=5000):
        self._annsal += rais

    def get_sal(self):
        return self._annsal


""" E1 = Employee("Abdul", "Rehman", 10000)
print(E1.get_sal())
E1.give_raise(200)
print(E1.get_sal())
 """
