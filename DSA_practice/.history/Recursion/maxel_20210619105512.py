l = map(int, list(input('Enter elements without any spaces: ')))
il = list(l)
print(il)


def maxel(il):
    lil = len(il)
    if il[0] == il[lil-1]:
        return il[0]
    else:
        if il[0] < il[1] or il[0] == il[1]:
            il.remove(il[0])
            print(il)
            maxel(il)
        else:
            il.remove(il[1])
            maxel(il)


print(maxel(il))
