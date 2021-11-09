import re
import string
i = input('Enter the string: ')
stri = str(string.punctuation)


def splch(str, stri):

    check = re.compile(stri)
    if check.search(str) == None:
        print("String is accepted")
    else:
        print("String is not accepted")


splch(i, stri)
