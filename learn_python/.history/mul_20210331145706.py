""" def multiply():
    inlist = input("nums: ")
    list = inlist.split()
    mul = 1
    sum = 0
    for x in list:
        sum += int(x)
        mul *= int(x)
    return mul, sum


print(multiply()) """


""" def sum(inlist):
    list = inlist.split()
    total = 0
    for x in list:
        total += x  # total = total + x
    return total


print(sum(input('Enter numbers by seperating with spaces: ')))  # "10 12 13"

"""


def rev_str(str):
    print(str)
    index = len(str)
    print(index)
    rstr = ''
    while index > 0:
        rstr = rstr + str[index - 1]
        print(rstr)
        index -= 1
        print(index)
    return rstr


print(rev_str(input('Enter the string: ')))

"""
x = input("kch bhi: ")
print(x)
spl = x.split()
print(spl)
for x in spl:
    print(int(x)) """
