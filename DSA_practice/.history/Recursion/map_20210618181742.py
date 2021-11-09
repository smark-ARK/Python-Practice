

l = map(int, list(input('elements do be:')))
l = list(l)


def sum(l):
    su = 0
    for i in l:
        su += i
    return su


a = map(sum, l)
print(int(a))
