

l = map(int, list(input('elements do be:')))
l = list(l)
ls = sum(l)
print(ls)

x = []


def su(i):
    if len(x) == 0:
        x.append(i)
        print(x)
        if len(x) == 2:
            x[0] += x[1]
            x.pop()
            print(x)


a = map(su, l)
c = list(a)
print(c)
