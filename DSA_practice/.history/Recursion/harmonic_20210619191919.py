import sys
import math
print(sys.getrecursionlimit())

a = int(input("Enter value of n: "))


def hor(a, hr, sum):

    if 1/a == 1/hr:
        print(sum)

    else:
        hr = hr+1
        z = 1/(hr)
        sum += z
        hor(a, hr, sum)


print(hor(a, 0, 0))
