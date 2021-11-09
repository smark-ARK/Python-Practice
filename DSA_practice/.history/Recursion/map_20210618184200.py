

l = map(int, list(input('elements do be:')))
l = list(l)

le = []


def sum(i):
    su = 0
    if len(le) <= 1:
        le.append(i)
    else:
        su += le[0]+i
        le.clear()

    return su


a = map(sum, l)
c = list(a)
print(c)
