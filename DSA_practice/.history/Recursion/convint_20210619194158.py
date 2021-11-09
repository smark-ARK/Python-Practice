lst = input('Enter Elements seperating with spaces: ')
lst = lst.split()
l = len(lst)-1


def convint(l, lst):
    if (type(lst[l]) == type('A')):
        le = int(lst[l])
        print(le)
        lst.insert(0, le)
        print(lst)
        lst.pop()
        convint(l, lst)
    return lst


print(convint(l, lst))
