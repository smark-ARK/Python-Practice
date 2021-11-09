import sys
import math
print(sys.getrecursionlimit())

a = int(input("Enter value of n: "))


def hor(a, hr, sum):

    if 1/a == 1/hr:
        return hr

    else:
        hr = hr+1
        z = 1/(hr)
        sum += z
        hor(a, z, sum)


print(hor(a, 0, 0))
