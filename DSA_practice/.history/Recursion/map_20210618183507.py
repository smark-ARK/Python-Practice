

l = map(int, list(input('elements do be:')))
l = list(l)


def sum(i):
    l = []
    su = 0
    while len(l) == 1:
        l.append(i)
        su += l[0]

    return su


a = map(sum, l)
c = list(a)
print(c)
