lst = [1, 2]


def unique(S, start, stop):


if stop − start <= 1:
    return True  # at most one item
elif not unique(S, start, stop−1):
    return False  # first part has duplicate
elif not unique(S, start+1, stop):
    return False  # second part has duplicate
else:
    return S[start] != S[stop−1]  # do first and last differ?

print(unique(lst, 0, 1))
""" 
def unique2(lst, start, stop):
    if stop-start <= 1:
        return True


print(unique2(lst, 0, 1))
 """
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
