def sumOfN(n):
    sum = 0
    for x in range(1, n):
        sum += x

    return sum


sumOfN(input('Enter the upper limit: '))
