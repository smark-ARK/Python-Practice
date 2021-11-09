

l = map(int, list(input('elements do be:')))
l = list(l)

a = map(sum, l)


def sum(l):
    su = 0
    for i in l:
        su += i
