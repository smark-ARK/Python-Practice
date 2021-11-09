

l = map(int, list(input('elements do be:')))
l = list(l)
ls = sum(l)
print(ls)

x = []


def su(i):
    if len(x) <= 1:
        x.append(i)
        print(x)


a = map(su, l)
c = list(a)
print(c)
