import re


def splch(str):

    check = re.compile('!"#$%&()*+, -.<= >?@ [\] ^ _`{ | }~')
    if (check.search(str) == None):
        print("String is accepted")
    else:
        print("String is not accepted")


if __name__ == '__main__':
    i = 'ISL$Engg'
    splch(i)
