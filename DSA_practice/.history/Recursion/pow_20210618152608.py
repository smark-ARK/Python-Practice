import sys
x = int(input('Val of x:'))
n = int(input('value of n: '))

sys.getrecursionlimit()
def pov(x, n):
    if n == 0:
        return 1
    elif x == 0:
        return 0
    else:
        return x*pov(x, n-1)


def main(x, n):
    return int(pow(x, n/2)**2)


print(main(x, n))
