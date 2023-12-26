class Node:
    def __init__(self, value,prev=None, next=None):
        self.value=value
        self.prev=prev
        self.next=next

    def __str__(self):
        return self.value
        
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def is_empty(self):
        return self.size==0
    
    def insertFront(self, x):
        new=Node(x)
        if self.is_empty():
            self.head=new
            self.tail=new
        else:
            new.next=self.head
            self.head=new
        self.size+=1
        return str(new)
    
    def insertEnd(self,x):
        new=Node(x)
        if self.is_empty():
            self.head=new
            self.tail=new
        else:
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
        self.size+=1
        return str(new)
    
    def removeFront(self):
        if self.is_empty():
            return "list is already empty"
        to_remove=self.head
        self.head=self.head.next
        self.head.prev=None
        self.size-=1
        return str(to_remove)

    def removeEnd(self):
        if self.is_empty():
            return "list is already empty"
        to_remove=self.tail
        self.tail=self.tail.prev
        self.tail.next=None
        self.size-=1
        return str(to_remove)
    
    def remove(self,x):
        if self.is_empty():
            return "Already Empty"
        curr=self.head
        while curr.next:
            if curr.value==x:
                break
            curr=curr.next
        if curr==None:
            return "Not Found"
    # def 