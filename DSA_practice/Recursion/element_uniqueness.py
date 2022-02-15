def uniqueness(arr):
    if len(arr) == 1:
        return True
    else:
        n = arr[0]
        ar = arr[1:]
        if n not in ar:
            return uniqueness(ar)
        else:
            return False


l = [1, 2, 3, 4]
print(uniqueness(l))

