import sys
import math
print(sys.getrecursionlimit())

a = int(input("Enter value of n: "))


def hor(a, hr, sum):

    if hr == round(1/a, 2):
        print(sum)

    else:
        hr = hr+1
        z = round(1/(hr), 2)
        sum += z
        hor(a, z, sum)


print(hor(a, 0, 0))
