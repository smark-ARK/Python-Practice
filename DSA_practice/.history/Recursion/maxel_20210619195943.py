l = input('Enter elements seperating with spaces: ')
l = l.split()
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


def minel(il):
    lil = len(il)
    if lil > 1:
        if il[0] > il[1] or il[0] == il[1]:
            il.remove(il[0])
            return minel(il)
        elif il[0] < il[1]:
            il.remove(il[1])
            return minel(il)
    else:
        return il[0]


print(minel(il))
print(maxel(il))
