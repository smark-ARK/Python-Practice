l = map(int, list(input('Enter elements without any spaces: ')))
il = list(l)
print(il)


def maxel(il):
    lil = len(il)
    if il[0] != il[lil-1]:
        if il[0] < il[1] or il[0] == il[1]:
            il.remove(il[0])
            maxel(il)
        elif il[0] > il[1]:
            il.remove(il[1])
            print(il)
            maxel(il)
        print(il[0])
    else:
        return il[0]


maxel(il)
