x = int(input('Val of x:'))
n = int(input('value of n: '))


def pov(x, n):
    if n == 0:
        return 1
    elif x == 0:
        return 0
    else:
        return x*pov(x, n-1)


def main():
    if x % 2 == 0:
        return pow(x, n/2)
