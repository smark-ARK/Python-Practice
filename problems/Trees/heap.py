class Heap:
    def __init__(self, size):
        self.list = [None] * (size + 1)
        self.heap_size = 0
        self.max_size = size + 1


def peek(root):
    if not root:
        return None
    return root.list[0]


def size(root):
    if not root:
        return None
    return root.heap_size


def levelorder_traversal(root):
    if not root:
        return
    for i in range(1, root.heap_size + 1):
        print(root.list[i])


def heapify_insert(root, index, type):
    if not root:
        return None
    if index <= 1:
        return
    parent_index = index // 2
    if type == "min":
        if root.list[index] < root.list[parent_index]:
            root.list[index], root.list[parent_index] = (
                root.list[parent_index],
                root.list[index],
            )
        heapify_insert(root, parent_index, type)
    else:
        if root.list[index] > root.list[parent_index]:
            root.list[index], root.list[parent_index] = (
                root.list[parent_index],
                root.list[index],
            )
        heapify_insert(root, parent_index, type)


def heapify_delete(root, index, type):
    left = 2 * index
    right = (2 * index) + 1

    swap = 0
    if root.heap_size < left:
        return
    elif root.heap_size == left:
        if type == "min":
            if root.list[index] > root.list[left]:
                root.list[index], root.list[left] = root.list[left], root.list[index]
            return
        else:
            if root.list[index] < root.list[left]:
                root.list[index], root.list[left] = root.list[left], root.list[index]
            return
    else:
        if type == "min":
            swap = left if root.list[left] <= root.list[right] else right

            if root.list[index] > root.list[swap]:
                root.list[index], root.list[swap] = root.list[swap], root.list[index]
        else:
            swap = left if root.list[left] >= root.list[right] else right
            if root.list[index] < root.list[swap]:
                root.list[index], root.list[swap] = root.list[swap], root.list[index]
        heapify_delete(root, swap, type)


def insert(root, val, type):
    if root.heap_size + 1 == root.max_size:
        return "Already Full"
    root.list[root.heap_size + 1] = val
    root.heap_size += 1
    heapify_insert(root, root.heap_size, type)
    return "inserted"


def delete(root, type):
    if root.heap_size == 0:
        return
    to_delete = root.list[1]
    root.list[1] = root.list[root.heap_size]
    root.list[root.heap_size] = None
    root.heap_size -= 1
    return to_delete


def delete_heap(root):
    root.list = None


new_heap = Heap(5)
insert(new_heap, 40, "min")
insert(new_heap, 50, "min")
insert(new_heap, 20, "min")
insert(new_heap, 10, "min")
print("\n----Levelorder-----")
levelorder_traversal(new_heap)
delete(new_heap, "min")
print("\n----Levelorder-----")
levelorder_traversal(new_heap)
