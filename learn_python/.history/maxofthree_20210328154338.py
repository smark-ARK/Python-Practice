def maxoftwo(x, y):
    if(x > y):
        return x
    return y


def maxofthree(x, y, z):
    return maxoftwo(x, maxoftwo(y, z))


maxofthree(55, 55.00001, 54.99999)
