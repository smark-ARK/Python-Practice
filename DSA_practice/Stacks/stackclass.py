class Stack:
    def __init__(self,Maxlen=None):
        self._data=[]
        self._Maxlen=Maxlen
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data)==0
    def is_full(self):
        return len(self._data)==self._Maxlen
    def push(self,k):
        if self.is_full():
            raise IndexError('Stack is already full')
        self._data.append(k)
    def top(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is already empty')
        return self._data.pop()
    
            
S=Stack(3)
S.push(3)
print(S.top())
S.push(5)
print(S.top())
S.push(8)
print(S.top())
#S.push(3)