

l = map(int, list(input('elements do be:')))
l = list(l)
ls = sum(l)
print(ls)

x = []


def su(i):
    if len(x) <= 2:
        x.append(i)
        print(x)
        l[0] += l[1]


a = map(su, l)
c = list(a)
print(c)
