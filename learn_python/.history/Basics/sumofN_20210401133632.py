def sumOfN(n):
    sum = 0
    for x in range(1, n):
        sum += x

    return sum


print('The Sum of', n, 'natural numbers is',
      sumOfN(int(input('Enter the upper limit: '))))
