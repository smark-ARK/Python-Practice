lst = list(input('Enter Elements without spaces: '))
l = len(lst)-1


def convint(l, lst):
    if (type(lst[l]) == type('A')):
        le = int(lst[l])
        lst.insert(0, le)
        lst.pop()
        convint(l, lst)
    return lst


inlst = convint(l, lst)
print(convint(l, lst))


def sumlst(inlst):
    if len(inlst) != 0:
        sum = int(sum)+inlst[0]+inlst[1]
        inlst.remove(inlst[0])
        inlst.remove(inlst[0])
        sumlst(inlst)
    print(sum)


sumlst(lst)
