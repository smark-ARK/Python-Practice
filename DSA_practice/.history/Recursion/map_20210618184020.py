

l = map(int, list(input('elements do be:')))
l = list(l)

le = []
su = 0


def sum(i):
    if len(l) == 0:
        l.append(i)
    else:
        su += l[0]+i
        l.clear()

    return su


a = map(sum, l)
c = list(a)
print(c)
