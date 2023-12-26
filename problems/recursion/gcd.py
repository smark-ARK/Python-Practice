def gcd(x,y):
    assert type(x) is int and x>=0 and type(y) is int and y>=0, "x and y must be positive integers!"
    assert x>y , "x must be greater than y!"
    if x==0:
        return y
    elif y==0:
        return x
    else:
        return gcd(y,x%y)
    

print(gcd(270,192))