import sys
sys.setrecursionlimit(100000)
S = [1, 2, 3, 4, 8, 7, 6, 5]

start = 0
stop = len(S)


def binary_sum(S, start, stop):

    if start >= stop:  # zero elements in slice
        return 0
    elif start == stop-1:  # one element in slice
        return S[start]
    else:  # two or more elements in slice
        mid = (start + stop) // 2
        print(mid)
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)


print(binary_sum(S, start, stop))
