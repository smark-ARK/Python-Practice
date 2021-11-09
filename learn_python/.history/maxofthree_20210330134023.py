def maxoftwo(x, y):
    if(x > y):
        return x
    return y


def maxofthree(x, y, z):
    return maxoftwo(x, maxoftwo(y, z))


print(maxofthree(55, 55.00001, 54.99999))


def max(a, b, c):
    if(a > b) and (a > c):
        print(a)
    elif(b > c) and (b > a):
        print(b)
    else:
        print(c)


max(10, 20, 5)
