class Caluculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        sum = int(self.a)+int(self.b)
        return sum

    def sub(self):
        return int(self.a)-int(self.b)

    def pro(self):
    return int(self.a)*int(self.b)


c1 = Caluculator(10, 20)
print(c1.sum())
