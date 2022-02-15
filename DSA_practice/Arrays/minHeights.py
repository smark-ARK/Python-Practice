def minHeights(arr, k):
    lent = len(arr)
    arr.sort()
    print(arr)
    for i in range(0, lent):
        if arr[i] - k <= 0:
            arr[i] = arr[i] + k
        else:
            arr[i] = arr[i] - k
        print(arr)
    dii = arr[-1] - arr[0]
    return dii, arr


print(minHeights([2, 6, 3, 4, 7, 2, 10, 3, 2, 1], 5))

