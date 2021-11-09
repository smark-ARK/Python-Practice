

l = map(int, list(input('elements do be:')))
l = list(l)


def sum(i):
    su = 0
    while i:
        su += i
    return su


a = map(sum, l)
c = int(a)
print(c)
