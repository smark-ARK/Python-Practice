lst = list(input('Enter Elements without spaces: '))
l = len(lst)-1


def convint(l, lst):
    if (type(lst[l]) == type('A')):
        le = int(lst[l])
        lst.insert(0, le)
        lst.pop()
        convint(l, lst)
    return lst


print(convint(l, lst))
sum = 0


def sumlst(lst):
    if lst[0] != lst[l]:
        sum = sum+lst[0]+lst[1]
        lst.remove(lst[0])
        lst.
