def good_fibonacci(n):

    if n <= 1:
    return (n, 0)
    else:
    (a, b) = good fibonacci(n−1)
    return (a+b, a)
