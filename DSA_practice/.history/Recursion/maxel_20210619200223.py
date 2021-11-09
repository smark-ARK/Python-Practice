l = input('Enter elements seperating with spaces: ')
l = l.split()
il = list(map(int, l))
il = list(map(int, l))
print(il)


def maxel(il):
    lil = len(il)
    if lil > 1:
        if il[0] < il[1] or il[0] == il[1]:
            il.remove(il[0])
            return maxel(il)
        elif il[0] > il[1]:
            il.remove(il[1])
            return maxel(il)
    else:
        return il[0]


def minel(li):
    lli = len(li)
    if lli > 1:
        if li[0] > li[1] or li[0] == li[1]:
            li.remove(li[0])
            return minel(li)
        elif li[0] < li[1]:
            li.remove(li[1])
            return minel(li)
    else:
        return li[0]


print(minel(li))
print(maxel(il))
