

l = map(int, list(input('elements do be:')))
l = list(l)

le = []

su = 0


def sum(i, int(su)):
    if len(le) == 0:
        le.append(i)
        su += le[0]+i
        le.clear()

    return su


a = map(sum, l)
c = list(a)
print(c)
