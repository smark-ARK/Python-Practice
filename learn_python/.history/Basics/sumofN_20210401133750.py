def sumOfN(n):
    sum = 1
    for x in range(1, n):
        sum += x

    return sum


print('The Sum of natural numbers is',
      sumOfN(int(input('Enter the upper limit: '))))
