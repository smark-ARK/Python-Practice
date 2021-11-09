lst = [1, 2]


def unique(lst, start, stop):

    if len(lst) == 1:
        return True  # at most one item
    elif not unique(lst, start, stop-1):
        return False  # first part has duplicate        return False  # second part has duplicate
    else:
        return lst[start] != lst[stop-1]  # do first and last differ?


print(unique(lst, 0, 1))

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
