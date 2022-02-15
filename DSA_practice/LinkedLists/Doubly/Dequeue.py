from DoublyLinkedBase import _DoublyLinkedBase


class Dequeue(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        return self.header.next.element

    def last(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        return self.trailer.prev.element

    def insert_first(self, e):
        self.insert(e, self.header, self.header.next)

    def insert_last(self, e):
        self.insert(e, self.trailer.prev, self.trailer)

    def delete_first(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.delete(self.header.next)

    def delete_last(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.delete(self.trailer.next)


DQ = Dequeue()
DQ.insert_first(7)
DQ.insert_first(8)
DQ.insert_last(9)
DQ.insert_last(10)
print(DQ.first())
print(DQ.last())
