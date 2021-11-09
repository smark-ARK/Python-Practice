

l = map(int, list(input('elements do be:')))
l = list(l)

le = []

su = 0


def sum(i):
    if len(le) <= 1:
        le.append(i)
        return
    else:
        for i in le:
            le[0] = le[0]+le[1]

    return le[0]


a = map(sum, l)
c = list(a)
print(c)
