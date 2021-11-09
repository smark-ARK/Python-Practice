

l = map(int, list(input('elements do be:')))
l = list(l)

le = []

su = 0


def sum(i):
    a = 0
    if len(le) == 0:
        le.append(i)
        a = i+le[0]
        le.clear()

    return a


a = map(sum, l)
c = list(a)
print(c)
