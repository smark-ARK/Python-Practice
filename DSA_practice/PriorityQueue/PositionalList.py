from DoublyLinkedBase import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    class Position:
        def __init__(self, container, node):
            self.container = container
            self.node = node

        def element(self):
            return self.node.element

        def __eq__(self, other):
            return type(other) is type(self) and other.node is self.node

        def __ne__(self, other):
            return not (other == self)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise ValueError(f"{p} must be a position")
        if p.container is not self:
            raise ValueError("Does not belongs to this list")
        if p.node.next is None:
            raise TypeError("P is no more a valid position")
        return p.node

    def _make_position(self, node):
        if node is self.header or node is self.trailer:
            return None
        return self.Position(self, node)

    def first(self):
        return self._make_position(self.header.next)

    def last(self):
        return self._make_position(self.trailer.prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node.prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node.next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.node.element
            cursor = self.after(cursor)

    def insert(self, e, pred, succ):
        node = super().insert(e, pred, succ)
        return self._make_position(node)

    def add_first(self, e):
        return self.insert(e, self.header, self.header.next)

    def add_last(self, e):
        return self.insert(e, self.trailer.prev, self.trailer)

    def add_before(self, e, p):
        node = self._validate(p)
        return self.insert(e, node.prev, node)

    def add_after(self, e, p):
        node = self._validate(p)
        return self.insert(e, node, node.next)

    def delete_pos(self, p):
        node = self._validate(p)
        return self.delete(node)

    def replace(self, e, p):
        original = self._validate(p)
        old_val = original.element
        original.element = e
        return old_val


pl = PositionalList()


def insertion_sort(pl):
    if len(pl) > 1:
        marker = pl.first()
        while marker != pl.last():
            pivot = pl.after(marker)
            value = pivot.element()
            # print(value)
            if value > marker.node.element:
                marker = pivot
            else:
                walk = marker
                while walk != pl.first() and pl.before(walk).node.element > value:
                    walk = pl.before(walk)
                pl.delete_pos(pivot)
                pl.add_before(value, walk)


"""
pl.add_first(9)
pl.add_first(4)
pl.add_first(6)
pl.add_first(1)
pl.add_first(8)
# pl.insert(7, pl.first(), pl.first().next)
print(pl.first().node.element)
# pl.delete_pos(pl.last())
print(pl.last().node.element)
insertion_sort(pl)
print(pl.first().node.element)
print(pl.last().node.element)
l = pl.__len__()
for v in range(l):
    gen = pl.__iter__()
    print(next(gen)) """

