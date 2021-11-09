lst = list(input('Enter Elements without spaces: '))
l = len(lst)-1
print(lst[2], l)


def convint(l, lst):
    while type(type(lst[l]) == type('A')):
        lst[l] = int(lst[l])
        convint(l-1, lst[l-1])
