

l = map(int, list(input('elements do be:')))
l = list(l)

le = []


def sum(i):
    su = 0
    if len(le) == 0:
        le.append(i)
    elif len(le) == 1:
        su += le[0]+i
    else:
        le.remove(le[0])

    return su


a = map(sum, l)
c = list(a)
print(c)
