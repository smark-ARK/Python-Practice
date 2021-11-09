lst = [1, 2]


def unique2(lst, start, stop):
    if stop-start <= 1:
        return True


print(unique2(lst, 0, 1))

""" def unique(lst):
    if len(lst) == 1:
        return True
    else:
        current = lst[0]
        remain = lst[1:]
        elementunique = current not in remain
        recursive = unique(remain)
        return elementunique and recursive


print(unique(lst))
 """
