

l = map(int, list(input('elements do be:')))
l = list(l)


def sum(i):
    l = []
    sum = 0
    while len(l) == 1:
        l.append(i)
        sum += l[0]

    return i


a = map(sum, l)
c = list(a)
print(c)
