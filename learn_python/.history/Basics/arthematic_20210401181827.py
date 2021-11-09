import math


def arth(a, b):
    sum = a+b
    diff = a-b
    pro = a*b
    div = a/b
    rem = a % b
    log = math.log10(a)
    pow = math.pow(a, b)
    print('Sum of two numbers: ', sum)
    print('Difference of two numbers: ', diff)
    print('Product of two numbers: ', pro)
    print('quotient of two numbers when divided: ', div)
    print('Remainder of two numbers when divided: ', rem)
    print('The result of log10 a: ', log)


i1 = int(input('Enter First Number: '))
i2 = int(input('Enter Second Number: '))
arth(i1, i2)
