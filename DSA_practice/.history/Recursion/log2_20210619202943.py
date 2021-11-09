n = int(input('Value of n: '))


def log2(n, k):
    if n == 1:
        return k
    else:
        log2(n/2, k+1)
        return
