import re
import string
i = input('Enter the string: ')


def splch(str):

    check = re.compile('!"#$%&()*+, -.<= >?@ [\] ^ _`{ | }~')
    if check.search(str) == None:
        print("String is accepted")
    else:
        print("String is not accepted")


splch(i)
