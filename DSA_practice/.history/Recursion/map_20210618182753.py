

l = map(int, list(input('elements do be:')))
l = list(l)


def sum(i):
    i += i
    return i


a = map(sum, l)
c = list(a)
print(c)
