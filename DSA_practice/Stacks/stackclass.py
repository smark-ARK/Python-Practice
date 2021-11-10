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
        return self.pop()
    
            
st=Stack()
st.push(5)
print(st.top())
print(st.__len__())