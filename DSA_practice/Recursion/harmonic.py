import sys
print(sys.getrecursionlimit())

a = int(input("Enter value of n: "))


def hor(a, hr, sum):

    if a == hr:
        return sum

    else:
        hr += 1
        z = 1/(hr)
        sum += z
        return hor(a, hr, sum)


print(hor(a, 0, 0))
