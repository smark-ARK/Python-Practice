def trans(s, t, tt):
    while s.__len__() != 0:
        t.push(S.pop())
    while t.__len__() != 0:
        tt.push(t.pop())
    while tt.__len__() != 0:
        s.push(tt.pop())
    return s


class Stack:
    def __init__(self, Maxlen=None):
        self._data = []
        self._Maxlen = Maxlen

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def is_full(self):
        return len(self._data) == self._Maxlen

    def push(self, k):
        if self.is_full():
            raise IndexError("Stack is already full")
        self._data.append(k)

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is already empty")
        return self._data.pop()


S = Stack()
S.push(6)
S.push(7)
S.push(4)
S.push(8)
S.push(9)
print(S.top())
T = Stack()
TT = Stack()
print(trans(S, T, TT).top())
