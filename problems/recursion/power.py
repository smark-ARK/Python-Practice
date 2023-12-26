def power(x,n):
    # assert type(x) is int, "x must be a positive integer!"
    assert type(n) is int, "n must be a positive integer!"
    if n==0:
        return 1
    elif n<0:
        return 1/(x*power(x,n+1))
    else:
        return x*power(x,n-1)

print(power(4,-1))