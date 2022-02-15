arr3 = []


def unionarr(arr1, arr2):
    arr1 += arr2
    return len(set(arr1))


print(unionarr([1, 2, 3], [1, 2, 3, 4, 5]))

