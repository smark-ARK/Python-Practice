class Caluculator:
    def __init__(self, a, b, choice):
        self.a = a
        self.b = b
        self.choice = choice

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


c1 = Caluculator(10, 20)
print(c1.sum())
