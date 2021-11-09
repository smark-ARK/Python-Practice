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
    elif x % 2 == 0:
        return x*(math.sqrt(pov2(x, n/2)))
    else:
        return math.sqrt(x*(pov2(x, n/2)))


print('power: ', math.sqrt(pov2(x, n)))
