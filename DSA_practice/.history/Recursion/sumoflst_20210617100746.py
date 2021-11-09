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


def sumlst(inlst, sum):

    if len(inlst) != 0:
        sum += inlst[0]
        print(sum)
        inlst.remove(inlst[0])
        sumlst(inlst, sum)
        print(sum)


print(sumlst(onlst, 0))
