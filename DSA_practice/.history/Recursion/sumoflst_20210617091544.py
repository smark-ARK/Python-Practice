lst = list(input('Enter Elements without spaces: '))
l = len(lst)-1
print(lst[2], l)


def convint(l, lst):
    if (type(lst[l]) == type('A')):
        le = int(lst[l])
        lst.insert(0, le)
        lst.pop()
        l -= 1
        convint(l, lst)
        print(lst)


convint(l, lst)
