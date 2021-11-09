x = int(input('Val of x:'))
n = int(input('value of n: '))


def pow(x, n):
    if n == 0:
        return 1
    elif x == 0:
        return 0
    else:
        return x*pow(x, n-1)
