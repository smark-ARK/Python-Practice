

l = list(input('Enter the sequence without spaces:'))
first = 0
last = len(l)-1


def rev(l, first, last):
    if first < last:
        l[first], l[last] = l[last], l[first]
        rev(l, first+1, last-1)
    return l


print('The Reversed Sequence', rev(l, first, last))
