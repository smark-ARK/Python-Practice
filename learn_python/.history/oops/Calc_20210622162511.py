class Caluculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        sum = int(a)+int(b)
        return sum

    def sub(self):
        return int(a)-int(b)

    def pro(self):
        return int(a)*int(b)


c1 = Caluculator(10, 20)
print(c1.sum())
