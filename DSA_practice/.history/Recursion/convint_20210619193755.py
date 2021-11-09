lst = input('Enter Elements without spaces: ')
l = len(lst)-1
lst = lst.split()


def convint(l, lst):
    if (type(lst[l]) == type('A')):
        le = int(lst[l])
        lst.insert(0, le)
        lst.pop()
        convint(l, lst)
    return lst
