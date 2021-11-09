import re
import string
i = input('Enter the string: ')


def splch(str):
    stri = str(string.punctuation)
    check = re.compile(stri)
    if check.search(str) == None:
        return "String is accepted"
    else:
        return "String is not accepted"


print(splch(i))
