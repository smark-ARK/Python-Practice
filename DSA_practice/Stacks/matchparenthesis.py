class Stack:
    def __init__(self):
        self._data=[]
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data)==0
    def push(self,k):
        self._data.append(k)
    def top(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is already empty')
        return self._data.pop()
    

def match(e):
    lefty='({['
    righty=')}]'
    S=Stack()
    for c in e:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False   
    return S.is_empty()
                
ex='([{}])'
print(match(ex))