def print_factors(x, y):

    l = []
    for i in range(1, x + 1):
        if x % i == 0:
            l.append(i)
    m = []
    for i in range(1, y + 1):
        if y % i == 0:
            m.append(i)
   `f=list(set(l).intersection(m))


num1 = int(input("Enter a number: "))  # 10
num2 = int(input("Enter a number: "))  # 15
print_factors(num1, num2)
