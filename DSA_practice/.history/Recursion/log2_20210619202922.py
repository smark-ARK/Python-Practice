n = int(input('Value of n: '))


def log2(n, k):
    if n == 1:
        return k
    else:
        log(n/2, k)
        return k += 1
