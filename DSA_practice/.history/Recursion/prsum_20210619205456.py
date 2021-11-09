m = int(input('Enter the alue of m: '))
n = int(input('Enter the alue of n: '))

m = 0


def sumpr(m, n):
    if n == 0:
        return m
    else:
        return sumpr(m+m, n-1)


print(sumpr(m, n))
