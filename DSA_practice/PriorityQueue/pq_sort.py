from UnsortedPriorityQueue import UnsortedPriorityQueue


def pq_sort(C: list):
    clen = len(C)
    PQ = UnsortedPriorityQueue()
    for i in range(0, clen):
        e = C.pop(0)
        PQ.add(e, e)
    for j in range(clen):
        (k, v) = PQ.remove_min()
        C.append(v)


l = [2, 12, 9, 7, 8]
pq_sort(l)
print(l)

