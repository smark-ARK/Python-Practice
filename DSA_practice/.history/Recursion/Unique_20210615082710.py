lst = [1, 4, 6, 7, 9]


def unique(lst):
    if len(lst) == 1:
        return True
    else:
        current = lst[0]
        remain = lst[1:]
        elementunique = current not in remain
        recursive = unique(remain)
        return elementunique and recursive
