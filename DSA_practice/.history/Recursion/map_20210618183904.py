

l = map(int, list(input('elements do be:')))
l = list(l)


def sum(i):
    l = []
    su = 0
    if len(l) == 0:
        l.append(i)
    else:
        su += l[0]+i
        l.clear()

    return su


a = map(sum, l)
c = list(a)
print(c)
