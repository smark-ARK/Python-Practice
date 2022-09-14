class _DoublyLinkedBase:
    class _Node:
        __slots__ = ["element", "prev", "next"]

        def __init__(self, element, prev, next):
            self.element = element
            self.prev = prev
            self.next = next

    def __init__(self):
        self.header = self._Node(None, None, None)
        self.trailer = self._Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def insert(self, e, pred, succ):
        newest = self._Node(e, pred, succ)
        pred.next = newest
        succ.prev = newest
        self._size += 1

    def delete(self, n):
        pred = n.prev
        succ = n.next
        pred.next = succ
        succ.prev = pred
        element = n.element
        self._size -= 1
        n.prev = n.next = n.element = None
        return element
