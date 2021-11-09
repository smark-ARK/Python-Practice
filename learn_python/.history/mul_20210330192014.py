""" def multiply():
    inlist = input("nums: ")
    list = inlist.split()
    mul = 1
    for x in list:
        mul *= int(x)
    return mul


print(multiply())
 """


def sum(list):
    total = 0
    for x in list:
        total += x
    return total


print(sum((10, 30, 83, 748, 7624, 778)))
