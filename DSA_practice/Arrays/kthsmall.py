def kthsmall(arr, k):
    arr.sort()
    e = arr[k - 1]
    return e


print(kthsmall([7, 10, 4, 20, 15], 4))

