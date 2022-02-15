class CircularlyQueue:
    class _Node:
        __slots__ = ["element", "next"]

        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        head = self._tail.next
        return head.element

    def dequeue(self):

        if self.is_empty():
            raise IndexError("queue is already empty")
        oldhead = self._tail.next
        if self._size == 1:
            self._tail = None
        else:
            self._tail.next = oldhead.next
        self._size -= 1
        return oldhead.element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest.next = newest
        else:
            newest.next = self._tail.next
            self._tail.next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail.next


cq = CircularlyQueue()

cq.enqueue(6)
print(cq.first())
cq.enqueue(7)
cq.enqueue(9)
print(cq.dequeue())

