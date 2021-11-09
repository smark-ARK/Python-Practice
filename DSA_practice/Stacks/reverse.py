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
l=[3,4,5,6,7,8,9]
s=Stack()
for i in l:
    s.push(i)
print(s.top())
i=0
while not s.is_empty():
    l[i]=s.pop()
    i+=1
    
print(l)