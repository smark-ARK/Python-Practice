import re
import string


def splch(str):

    check = re.compile('!"#$%&()*+, -.<= >?@ [\] ^ _`{ | }~')
    if check.search(str) == None:
        print("String is accepted")
    else:
        print("String is not accepted")


i = 'ISL$Engg'
splch(i)
