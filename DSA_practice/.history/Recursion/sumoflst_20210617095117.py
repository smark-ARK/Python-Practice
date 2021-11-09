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


def sumbhadkhau():
    def sumlst(inlst):

        if len(inlst) != 0:
            sum += inlst[0]+inlst[1]
            print(sum)
            inlst.remove(inlst[0])
            inlst.remove(inlst[0])
            print(inlst)
            sumlst(inlst, 0)
        print(sum)


sumlst(lst, sum)
