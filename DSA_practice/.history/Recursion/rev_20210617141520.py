l = [1, 2, 4, 5, 8]
first = 0
last = len(l)-1


def rev(l, first, last):
    if first < last:
        l[first], l[last] = l[last], l[first]
        rev(l, first+1, last-1)
        print(l)
