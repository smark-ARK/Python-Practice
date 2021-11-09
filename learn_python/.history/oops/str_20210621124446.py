import re
import string
i = input('Enter the string: ')


def splch(str):
    check = re.compile(string.punctuation)
    if check.search(str) == None:
        return "String is accepted"
    else:
        return "String is not accepted"


print(splch(i))
