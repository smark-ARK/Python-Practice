def multiply(list):
    mul = 1
    for x in list:
        mul *= x
    return mul


print(multiply((3, 4, 5, 3, 6, 7, 8, 4, 100)))
