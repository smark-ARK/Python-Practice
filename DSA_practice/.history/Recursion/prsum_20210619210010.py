m = int(input('Enter the alue of m: '))
n = int(input('Enter the alue of n: '))


def sumpr(m, n, k):
    if n == 0:
        return k
    else:

        return sumpr(m, n-1, k+m)


print(sumpr(m, n, 0))
