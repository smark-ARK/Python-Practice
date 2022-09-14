from queue import Empty
from PriorityQueueBase import PriorityQueueBase


class HeapBottomUP(PriorityQueueBase):
    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return (2 * j) + 1

    def _right(self, j):
        return (2 * j) + 2

    def _has_left(self, j):
        return self._left(j) < len(self.data)

    def _has_right(self, j):
        return self._right(j) < len(self.data)

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._Item.__it__(self.data[j], self.data[parent]):
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                small_child = right
                if self._Item.__it__(self.data[left], self.data[right]):
                    small_child = left
            if self._Item.__it__(self.data[small_child], self.data[j]):
                self._swap(self.data[small_child], self.data[j])
                self._downheap(small_child)

    def __init__(self, contents=()):
        self.data = [self._Item(k, v) for k, v in contents]
        if len(self.data) > 1:
            self.heapify()

    def heapify(self):
        start = self._parent(len(self.data) - 1)
        for i in range(start, -1, -1):
            self._downheap(i)

    def add(self, k, v):
        item = self._Item(k, v)
        self.data.append(item)
        self._upheap(len(self.data) - 1)

    def min(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        minimum = self.data[0]
        return (minimum.key, minimum.value)

    def remove_min(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        self._swap(0, len(self.data) - 1)
        removed = self.data.pop()
        self._downheap(0)
        return (removed.key, removed.value)


contents = [(1, "A"), (2, "R")]
HPQ = HeapBottomUP(contents=contents)


print(HPQ.remove_min())
# print(HPQ.remove_min())
