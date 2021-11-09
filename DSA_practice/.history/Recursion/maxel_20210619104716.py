l = map(int, list(input('Enter elements without any spaces: ')))
il = list(l)
print(il)
lil = len(il)


def maxel(il, lil):
    if il[0] == il[lil-1]:
        return il[0]
    else:
        if il[0] < il[1]:
            il.remove(il[0])
            maxel(il, lil)
        elif il[0] > il[1]:
            il.remove[il[1]]
            maxel(il, lil)
        else:
            il.remove(il[0])
