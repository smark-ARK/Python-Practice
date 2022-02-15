import time


def rearreven(arr, i, odd: list = []):
    if len(arr) == 1:
        return arr
    else:
        if arr[i] % 2 == 0:
            try:
                if i == len(arr) - 1:
                    arr = arr + odd
                    return arr
                else:
                    return rearreven(arr, i + 1, odd)
            except IndexError:
                arr = arr + odd
                return arr
        else:
            o = arr.pop(i)
            odd.append(o)
            return rearreven(arr, i, odd)


start = time.time()
l = [2, 3, 4, 5, 6, 7]
print(rearreven(l, 0))
end = time.time()
print(f"duration: {end-start}")

