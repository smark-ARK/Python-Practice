class LinkedQueue:
    class _Node:
        __slots__ = ["element", "next"]

        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        return self._head.element

    def enqueue(self, e):
        new = self._Node(e, None)
        if self.is_empty():
            self._head = new
        else:
            self._tail.next = new
        self._tail = new
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is already Empty")
        answer = self._head.element
        self._head = self._head.next
        self._size -= 1
        return answer


LQ = LinkedQueue()
LQ.enqueue(5)
LQ.enqueue(6)
LQ.enqueue(9)
print(LQ.first())
print(LQ.dequeue())
print(LQ.first())
