

l = map(int, list(input('elements do be:')))
l = list(l)
ls = sum(l)
print(ls)

x = []


def su(i):
    x.append(i)
    if len(x) < 2:
        return
    else:
        x[0] += x[1]
        x.pop()
    return x[0]


a = map(su, l)
c = list(a)
print(c[len(c)-1])

