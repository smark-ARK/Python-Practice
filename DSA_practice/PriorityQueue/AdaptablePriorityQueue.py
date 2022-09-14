from matplotlib.ticker import Locator
from HeapPriorityQueue import HeapPriorityQueue


class AdaptablePriorityQueue(HeapPriorityQueue):
    class Locator(HeapPriorityQueue._Item):
        def __init__(self, key, value, index):
            super().__init__(key, value)
            self.index = index

    def _swap(self, i, j):
        super()._swap(i, j)
        self.data[i].index = i
        self.data[j].index = j

    def bubble(self, j):
        if j > 0 and self.data[j].key < self.data[self._parent(j)].key:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self, k, v):
        token = self.Locator(k, v, len(self.data))
        self.data.append(token)
        self._upheap(token.index)
        return token

    def update(self, loc, nk, nv):
        j = loc.index
        if not (0 <= j < len(self.data) and self.data[j] is loc):
            raise ValueError("Item not valid")
        loc.key = nk
        loc.value = nv
        self.bubble(j)
        return (loc.key, loc.value)

    def remove(self, loc):
        j = loc.index
        if not (0 <= j < len(self.data) - 1 and self.data[j] is loc):
            raise ValueError("Item not valid")
        if j == len(self.data) - 1:
            popped = self.data.pop()
        self._swap(j, len(self.data) - 1)
        popped = self.data.pop()
        self.bubble(j)
        return (popped.key, popped.value)


APQ = AdaptablePriorityQueue()

a = APQ.add(3, 5)
b = APQ.add(5, 5)
c = APQ.add(1, 5)

print(APQ.update(a, 2, 8))
print(APQ.remove(b))

