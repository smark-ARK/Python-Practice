import sys
import math
print(sys.getrecursionlimit())

a = int(input("Enter value of n: "))


def hor(a, hr, sum):

    if hr == a:
        print(sum)
        return sum

    else:
        hr = hr+1
        z = 1/(hr)
        #hr = hr+1
        sum += z
        hor(a, hr, sum)


print(hor(a, 0, 0))
