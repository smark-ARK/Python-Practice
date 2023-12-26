from SinglyLinkedList import LinkedList


def nth_to_last(ll, n):
    left = ll.head
    right = ll.head
    for i in range(n):
        right=right.next

    while right:
        left=left.next
        right=right.next

    return left

c=LinkedList()
c.generate(10,6,19)
print(c)
print(nth_to_last(c,3))