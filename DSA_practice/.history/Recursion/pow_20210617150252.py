x = int(input('Val of x:'))
n = int(input('value of n: '))


def pov(x, n):
    if n == 0:
        return 1
    elif x == 0:
        return 0
    else:
        return x*pov(x, n-1)


print(pov(x, n))
