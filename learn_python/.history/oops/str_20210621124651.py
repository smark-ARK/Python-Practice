import re
import string
i = input('Enter the string: ')
stri = str(string.punctuation)


def splch(str, stri):

    check = re.compile(stri)
    if check.search(str) == None:
        return "String is accepted"
    else:
        return "String is not accepted"


print(splch(i, stri))
