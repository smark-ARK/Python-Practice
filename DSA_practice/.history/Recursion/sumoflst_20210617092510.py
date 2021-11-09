lst = list(input('Enter Elements without spaces: '))
l = len(lst)-1


def convint(l, lst):
    if (type(lst[l]) == type('A')):
        le = int(lst[l])
        print(le)
        lst.insert(0, le)
        lst.pop()
        convint(l, lst)
    return lst


convint(l, lst)
