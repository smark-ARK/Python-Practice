from queue import Empty


class SinglyLinkedList:
    class _Node:
        __slots__ = ["element", "next"]

        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise Empty("List is Empty")
        return self.head.element

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        answer = self.head.element
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self.size += 1

    def sec_last(self):
        p1 = self.head
        p2 = self.head.next
        for i in range(0, self.size):
            if p2 == self.tail:
                return p1.element
            else:
                p1 = p1.next
                p2 = p2.next


q1 = SinglyLinkedList()
q1.enqueue(5)
q1.enqueue(6)
q1.enqueue(7)
print(q1.sec_last())
