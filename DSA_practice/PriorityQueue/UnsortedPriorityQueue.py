from PriorityQueueBase import PriorityQueueBase
from PositionalList import PositionalList


class UnsortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self.data = PositionalList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return self.__len__() == 0

    def _find_min(self):
        if self.is_empty():
            raise ValueError("Queue is Empty")
        small = self.data.first()
        walk = self.data.after(small)

        while walk is not None:
            if self._Item.__it__(walk.element(), small.element()):
                small = walk
            walk = self.data.after(walk)
        return small

    def add(self, k, e):
        newest = self._Item(k, e)
        self.data.add_last(newest)

    def min(self):
        minimum = self._find_min()
        Item = minimum.element()
        return (Item.key, Item.value)

    def remove_min(self):
        minimum = self._find_min()
        Item = self.data.delete_pos(minimum)
        return (Item.key, Item.value)


UPQ = UnsortedPriorityQueue()
UPQ.add(3, 5)
UPQ.add(1, 9)
UPQ.add(2, 0)

print(UPQ.min())
