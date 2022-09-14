from collections.abc import MutableMapping


class UnsortedMap(MutableMapping):
    class _Item:
        __slots__ = ("key", "value")

        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __eq__(self, other):
            return self.key == other.key

        def __ne__(self, other):
            return not (self == other)

        def __it__(self, other):
            return self.key < other.key

    def __init__(self):
        self.table = []

    def __getitem__(self, k):
        for item in self.table:
            if item.key == k:
                return item.value

        raise KeyError(f"key {repr(k)} does not exists")

    def __setitem__(self, k, v):
        for item in self.table:
            if item.key == k:
                item.value = v
                return
        else:
            self.table.append(self._Item(k, v))

    def __delitem__(self, k):
        for item in self.table:
            if item.key == k:
                self.pop(self.table.index(item))
                return
        raise KeyError(f"key {repr(k)} does not exists")

    def __len__(self) -> int:
        return len(self.table)

    def __iter__(self):
        for item in self.table:
            yield item


UM = UnsortedMap()
UM.__setitem__(1, 5)
UM.__setitem__(4, 7)
UM.__setitem__(6, 9)

print(UM.__len__())

print(UM.__getitem__(1))
print(UM.__getitem__(6))
print(UM.__contains__(6))
