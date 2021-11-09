def sumOfN(n):
    sum = 0
    for x in range(1, n):
        sum += (x+1)

    return sum


print('The Sum of natural numbers is',
      sumOfN(int(input('Enter the upper limit: '))))
