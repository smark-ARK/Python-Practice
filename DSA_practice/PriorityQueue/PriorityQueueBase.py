class PriorityQueueBase:
    class _Item:
        __slots__ = "key", "value"

        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __it__(self, other):
            return self.key < other.key

    def is_empty(self):
        return len(self.data) == 0

