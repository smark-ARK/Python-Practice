def good_fibonacci(n):

    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n-1)
        print(a, b)
        print(a+b, a)
        return (a+b, a)


print(good_fibonacci(5))  # 011235
