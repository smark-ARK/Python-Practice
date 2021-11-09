def arth(a, b):
    sum = a+b
    diff = a-b
    pro = a*b
    div = a/b
    rem = a % b
    pow = math.pow(a, b)
    print('Sum of two numbers: ', sum)
    print('Difference of two numbers: ', diff)
    print('Product of two numbers: ', pro)


i1 = int(input('Enter First Number: '))
i2 = int(input('Enter Second Number: '))
arth(i1, i2)
