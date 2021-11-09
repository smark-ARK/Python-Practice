

l = map(int, list(input('elements do be:')))
l = list(l)

su = 0


def sum(i):

    su += i
    return su


a = map(sum, l)
c = list(a)
print(c)
