import math
x = int(input('Val of x:'))
n = int(input('value of n: '))


def pov2(x, n):
    if n == 0:
        return 1
    elif x == 0:
        return 0
    elif x % 2 == 0:
        return math.sqrt(pov2(x, n/2))
    else:
        return x*math.sqrt(pov2(x, n/2))
