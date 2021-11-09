

l = map(int, list(input('elements do be:')))
l = list(l)

le = []

su = 0


def sum(i):
    if len(le) == 0:
        le.append(i)
    elif len(le) == 1:

    else:
        le.remove(le[0])

    return su


a = map(sum, l)
c = list(a)
print(c)
