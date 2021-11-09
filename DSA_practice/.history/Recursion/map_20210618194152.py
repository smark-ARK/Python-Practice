

l = map(int, list(input('elements do be:')))
l = list(l)
ls = sum(l)
print(ls)

x = []


def su(i):
    if len(x) == 2:
        x.append(i)
        print(x)
        x[0] += x[1]
        x.pop()
    return l[0]


a = map(su, l)
c = list(a)
print(c)
