
class Stack:
    def __init__(self,Maxlen=None):
        self._data=0
        self._Maxlen=Maxlen
        self._Sarr=[None]*Maxlen
    def __len__(self):
        return self._data
    def is_empty(self):
        return self._data==0
    def is_full(self):
        return self._data==self._Maxlen
    def push(self,k):
        if self.is_full():
            raise IndexError('Stack is already full')
        self._Sarr[self._data]=k
        self._data+=1
    def top(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._Sarr[self._data-1]
    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is already empty')
        i = self._Sarr[self._data-1]
        self._Sarr[self._data-1]=None
        self._data-=1
        return i

S=Stack(3)
S.push(3)
print(S.top())
S.push(5)
print(S.top())
S.push(8)
print(S.top())
#S.push(3)
print(S.pop())
