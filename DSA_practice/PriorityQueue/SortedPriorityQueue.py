from queue import Empty

from PriorityQueueBase import PriorityQueueBase
from PositionalList import PositionalList


class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self.data = PositionalList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return self.__len__() == 0

    def add(self, k, e):
        newest = self._Item(k, e)
        walk = self.data.last()
        while walk is not None and self._Item.__it__(newest, walk.element()):
            walk = self.data.before(walk)
        if walk is None:
            self.data.add_first(newest)
        else:
            self.data.add_after(newest, walk)

    def min(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        minimum = self.data.first()
        return (minimum.element().key, minimum.element().value)

    def remove_min(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        minimum = self.data.delete_pos(self.data.first())
        return (minimum.element().key, minimum.element().value)


SPQ = SortedPriorityQueue()
SPQ.add(3, 5)
SPQ.add(1, 9)
SPQ.add(2, 0)

print(SPQ.min())
