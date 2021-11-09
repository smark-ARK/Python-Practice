n = int(input('Value of n: '))


def log2(n, k):
    if n == 1:
        return k
    else:
        return log2(n/2, k+1)


print(log2(n, 0))
