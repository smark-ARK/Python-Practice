class CQueue:
    def __init__(self,Dcap):
        self._Dcap=Dcap
        self._data=[None]*Dcap
        self._size=0
        self._front=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self.__len__()==0
    def first(self):
        if self.is_empty():
            raise IndexError('Queue is Empty')
        return self._data[self._front]
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is Empty')
        answer=self._data[self._front]
        self._data[self._front]=None
        self._front=(self._front+1)%len(self._data)
        return answer
    def enqueue(self,e):
        if self._size==len(self._data):
            self._resize(2*self._Dcap)
        avail=(self._front+self._size)%len(self._data)
        self._data[avail]=e
        self._size+=1
            
    def resize(self,cap):
        old=self._data
        self._data=[None]*cap
        walk=self._front
        for k in range(len(old)):
            self._data[k]=old[walk]
            walk=(1+walk)%len(old)
        self._front=0
        
q=CQueue(10)
q.enqueue(3)
q.enqueue(4)
q.enqueue(6)
q.enqueue(5)
q.enqueue(8)
q.enqueue(9)
print(q.first())
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
print(q.first())
