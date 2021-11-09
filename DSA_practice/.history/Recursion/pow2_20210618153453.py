import math
import sys
x = int(input('Val of x:'))
n = int(input('value of n: '))

sys.setrecursionlimit(100000)


def pov2(x, n):
    if n == 0:
        return 1
    elif x == 0:
        return 0
    elif n % 2 == 0:
        return ((pov2(x, int(n/2)))**2)
    else:
        return x*((pov2(x, int(n/2)))**2)


print('power: ', pov2(x, n))
