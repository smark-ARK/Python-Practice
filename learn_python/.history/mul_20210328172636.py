def multiply(list):
    mul = 1
    for x in list:
        mul *= x
    return mul


print(multiply((3, 4, 5, 3, 6, 7, 8, 4, 100)))


def sum(list):
    total = 0
    for x in list:
        total += x
    return total


print(sum((10, 30, 83, 748, 7624, 778)))
