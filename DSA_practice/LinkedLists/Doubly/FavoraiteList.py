from PositionalList import PositionalList


class FavoraiteList:
    class _item:
        __slots__ = ["value", "count"]

        def __init__(self, e):
            self.value = e
            self.count = 0

    def find_position(self, e):
        walk = self.data.first()
        while walk is not None and walk.element().value != e:
            walk = self.data.after(walk)
        return walk

    def move_up(self, p):
        if p != self.data.first():
            count = p.element().count
            walk = self.data.before(p)
            if count > walk.element().count:
                cnt = self.data.before(walk).element().count
                while walk != self.data.first() and count > cnt:
                    walk = self.data.before(walk)
                self.data.add_before(self.data.delete_pos(p), walk)

    def __init__(self):
        self.data = PositionalList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return self.__len__() == 0

    def access(self, e):
        p = self.find_position(e)
        if p is None:
            p = self.data.add_last(self._item(e))
            p = self.find_position(e)
        p.element().count += 1
        self.move_up(p)

    def remove(self, e):
        pos = self.find_position(e)
        if pos is None:
            raise ValueError("Invalid Position")
        self.data.delete_pos(pos)

    def top(self, k):
        if not 1 < k <= len(self.data):
            raise IndexError(f"{k} is not a valid index")
        walk = self.data.first()
        for i in range(k):
            item = walk.element()
            yield item.value
            walk = self.data.after(walk)


fl1 = FavoraiteList()

fl1.access(10)
fl1.access(11)
fl1.access(12)
fl1.access(12)
fl1.access(12)
fl1.access(12)
fl1.access(12)
fl1.access(12)
fl1.remove(12)
gen = fl1.top(2)
print(next(gen))
print(next(gen))
