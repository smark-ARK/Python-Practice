from problems.Queues import QueueLinkedList


class AVLNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 1


def preorder_traversal(root):
    if root is None:
        return
    print(root.data)
    preorder_traversal(root.left)
    preorder_traversal(root.right)


def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.data)
    inorder_traversal(root.right)


def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data)


def levelorder_traversal(root):
    if root is None:
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


def search(root, val):
    if root is None:
        return
    if val == root.data:
        print("success")
        return
    elif val < root.data:
        if root.left is None:
            print("Not Found")
            return
        else:
            search(root.left, val)
    else:
        if root.left is None:
            print("Not Found")
            return
        else:
            search(root.right, val)


def min_node(root):
    current = root
    while current.left is not None:
        current = current.left
    return current


def get_height(root):
    if not root:
        return 0
    return root.height


def right_rotate(unbalanced):
    new_root = unbalanced.left
    unbalanced.left = unbalanced.left.right
    new_root.right = unbalanced
    unbalanced.height = 1 + max(
        get_height(unbalanced.left), get_height(unbalanced.right)
    )
    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))
    return new_root


def left_rotate(unbalanced):
    new_root = unbalanced.right
    unbalanced.right = unbalanced.right.left
    new_root.left = unbalanced
    unbalanced.height = 1 + max(
        get_height(unbalanced.left), get_height(unbalanced.right)
    )
    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))
    return new_root


def get_balance(root):
    if not root:
        return 0
    return get_height(root.left) - get_height(root.right)


def insert(root, val):
    if not root:
        return AVLNode(val)
    elif val < root.data:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)
    if balance > 1 and val < root.left.data:
        return right_rotate(root)
    if balance > 1 and val > root.left.data:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and val > root.right.data:
        return left_rotate(root)
    if balance < -1 and val < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root


new_avl = AVLNode(10)
new_avl = insert(new_avl, 20)
new_avl = insert(new_avl, 30)
new_avl = insert(new_avl, 40)
print(new_avl.data)
new_avl = insert(new_avl, 50)
print(new_avl.data)
new_avl = insert(new_avl, 35)
print(new_avl.data)
print("\n----Preorder-----")
preorder_traversal(new_avl)
print("\n----Inorder-----")
inorder_traversal(new_avl)
print("\n----Postorder-----")
postorder_traversal(new_avl)
print("\n----Levelorder-----")
levelorder_traversal(new_avl)
print("\n-----Search-----")
search(new_avl, 10)
