""" def multiply():
    inlist = input("nums: ")
    list = inlist.split()
    mul = 1
    for x in list:
        mul *= int(x)
    return mul


print(multiply())
 """

""" 
def sum(inlist):
    list = inlist.split()
    total = 0
    for x in list:
        total += x  # total = total + x
    return total


print(sum(input('Enter numbers by seperating with spaces: ')))  # "10 12 13"


def rev_str(str):
    index = len(str)
    rstr = ''
    while index > 0:
        rstr = rstr + str[index - 1]
        index -= 1
    return rstr


print(rev_str(input('Enter the string: ')))
 """

x = input("kch bhi: ")
x.split()
