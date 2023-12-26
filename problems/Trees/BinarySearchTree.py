from problems.Queues import QueueLinkedList


class BSTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def insert(root, val):
    if root.data == None:
        root.data = val
    elif val <= root.data:
        if root.left is None:
            root.left = BSTNode(val)
        else:
            insert(root.left, val)
    else:
        if root.right is None:
            root.right = BSTNode(val)
        else:
            insert(root.right, val)
    return "Node added successfully"


def preorder_traversal(root):
    if not root or root.data == None:
        return
    print(root.data)
    preorder_traversal(root.left)
    preorder_traversal(root.right)


def inorder_traversal(root):
    if not root or root.data == None:
        return
    inorder_traversal(root.left)
    print(root.data)
    inorder_traversal(root.right)


def postorder_traversal(root):
    if not root or root.data == None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data)


def levelorder_traversal(root):
    if not root or root.data == None:
        return
    else:
        q = QueueLinkedList.Queue()
        q.enqueue(root)
        while not q.isEmpty():
            node = q.dequeue()
            print(node.value.data)
            if node.value.left is not None:
                q.enqueue(node.value.left)
            if node.value.right is not None:
                q.enqueue(node.value.right)
        return


def search(root, val):
    if root.data is None:
        print("Not Found")
        return
    if root.data == val:
        print("Success")
        return
    elif val < root.data:
        if root.left is None:
            print("Not Found")
            return
        else:
            search(root.left, val)
    else:
        if root.right is None:
            print("Not Found")
            return
        else:
            search(root.right, val)


def min_node(root):
    current = root
    while current.left is not None:
        current = current.left
    return current


def delete_node(root, value):
    if root is None:
        return root
    if value < root.data:
        root.left = delete_node(root.left, value)
    elif value > root.data:
        root.right = delete_node(root.right, value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        if root.right is None:
            temp = root.left
            root = None
            return temp
        temp = min_node(root.right)
        root.data = temp.data
        root.right = delete_node(root.right, temp.data)
    return root


def delete_bst(root):
    if not root:
        return
    root.left = None
    root.right = None
    root = None
    return


new_bst = BSTNode(None)
print(insert(new_bst, 100))
print(insert(new_bst, 150))
print(insert(new_bst, 70))
print(insert(new_bst, 90))
print(insert(new_bst, 120))
print("\n----Preorder-----")
preorder_traversal(new_bst)
print("\n----Inorder-----")
inorder_traversal(new_bst)
print("\n----Postorder-----")
postorder_traversal(new_bst)
print("\n----Levelorder-----")
levelorder_traversal(new_bst)
print("\n-----Search-----")
search(new_bst, 200)
delete_node(new_bst, 100)
print("\n----Levelorder-----")
levelorder_traversal(new_bst)
