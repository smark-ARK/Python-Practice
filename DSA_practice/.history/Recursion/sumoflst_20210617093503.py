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


def sumlst(lst):
    sum = 0
    if len(lst) != 0:
        sum = sum+lst[0]+lst[1]
        lst.remove(lst[0])
        lst.remove(lst[0])
        sumlst(lst)
    print(sum)


sumlst(lst)
