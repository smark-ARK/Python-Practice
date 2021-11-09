class Caluculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return int(self.a)+int(self.b)

    def sub(self):
        return int(self.a)-int(self.b)

    def pro(self):
        return int(self.a)*int(self.b)

    def div(self):
        return int(self.a)/int(self.b)

    def modu(self):
        return int(self.a) % int(self.b)

    def exp(self):
        return int(self.a)**int(self.b)

    def menu(self):
        print('Enter the choice: \n1. Add a and b: \n2. subtract a and b: \n3. multiply a and b: \n4. divide a and b: \n5. remainder a / b: \n6. Exponent of a and b: ')
        c = int(input('What operation do u want to perform: ')
        if c > 0:




c1=Caluculator(10, 20)
print(c1.menu())
