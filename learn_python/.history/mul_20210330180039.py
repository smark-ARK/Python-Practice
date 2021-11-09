def multiply(list):
    list = input("List: ")
    mul = 1
    for x in list:
        mul *= x
    return mul


print(multiply())


def sum(list):
    total = 0
    for x in list:
        total += x
    return total


print(sum((10, 30, 83, 748, 7624, 778)))
