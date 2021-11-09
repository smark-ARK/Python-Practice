n = int(input('Value of n: '))


def log2(n, k):
    if n == 1:
        return k
    else:
        k += n/2
        return log(n, k)
