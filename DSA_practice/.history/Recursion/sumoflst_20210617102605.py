lst = list(input('Enter Elements without spaces: '))
l = len(lst)-1


def convint(l, lst):
    if (type(lst[l]) == type('A')):
        le = int(lst[l])
        lst.insert(0, le)
        lst.pop()
        convint(l, lst)
    return lst


onlst = convint(l, lst)
print(convint(l, lst))

l = len(onlst)


def sumlst(inlst, l):

    if len(inlst) == 0:
        return 0
    else:
        return sumlst()


print(sumlst(onlst, 0))
