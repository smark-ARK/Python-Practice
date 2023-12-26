from problems.Queues import QueueLinkedList
class TreeNode:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None


new_bt=TreeNode("Drinks")
lc=TreeNode("Hot")
rc=TreeNode("Cold")

new_bt.left=lc
new_bt.right=rc 

def preorder_traversal(root):
    if not root:
        return
    print(root.data)
    preorder_traversal(root.left)
    preorder_traversal(root.right)



def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print(root.data)
    inorder_traversal(root.right)

def postorder_traversal(root):
    if not root:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data)

def levelorder_traversal(root):
    if not root:
        return
    else:
        q=QueueLinkedList.Queue()
        q.enqueue(root)
        while not q.isEmpty():
            node=q.dequeue()
            print(node.value.data)
            if node.value.left!=None:
                q.enqueue(node.value.left)
            if node.value.right!=None:
                q.enqueue(node.value.right)

def search_bt(root, x):
    if not root:
        return
    else:
        q=QueueLinkedList.Queue()
        q.enqueue(root)
        while not q.isEmpty():
            node=q.dequeue()

            if node.value.data == x:
                return "success"
            if node.value.left !=None:
                q.enqueue(node.value.left)
            if node.value.right !=None:
                q.enqueue(node.value.right)
        return "Not Found"

def insert_bt(root, newNode):
    if not root:
        root=newNode
    else:
        q=QueueLinkedList.Queue()
        q.enqueue(root)
        while not q.isEmpty():
            node=q.dequeue()
            if node.value.left != None:
                q.enqueue(node.value.left)
            else:
                node.value.left = newNode
                return "added"
            if node.value.right != None:
                q.enqueue(node.value.right)
            else:
                node.value.right = newNode
                return "added"

def deepest_node(root):
    if not root:
        return
    else:
        q=QueueLinkedList.Queue()
        q.enqueue(root)
        while not q.isEmpty():
            node = q.dequeue()
            if node.value.left !=None:
                q.enqueue(node.value.left)
            if node.value.right !=None:
                q.enqueue(node.value.right)  
        return node.value      

def delete_deepest(root, deepest):
    if not root:
        return
    else:
        q=QueueLinkedList.Queue()
        q.enqueue(root)
        while not q.isEmpty():
            node = q.dequeue()
            if node.value is deepest:
                node.value=None
                return
            if node.value.left !=None:
                if node.value.left is deepest:
                    node.value.left=None
                    return
                else:
                    q.enqueue(node.value.left)
            if node.value.right !=None:
                if node.value.right is deepest:
                    node.value.left=None
                else:
                    q.enqueue(node.value.right)



def delete_node(root, x):
    if not root:
        return
    else:
        q=QueueLinkedList.Queue()
        q.enqueue(root)
        while not q.isEmpty():
            node = q.dequeue()
            if node.value.data == x:
                deepest=deepest_node(root)
                node.value.data=deepest.data
                delete_deepest(root, deepest)
                return f"Deleted: {node.value.data}"
            if node.value.left != None:
                q.enqueue(node.value.left)
            if node.value.right!=None:
                q.enqueue(node.value.right)
        return "could not delete"
    
def delete_bt(root):
    root.left=None
    root.right=None
    root.data=None
    return "deleted entire tree"

print("\n----Preorder-----")
preorder_traversal(new_bt)
print("\n-----Inorder------")
inorder_traversal(new_bt)
print("\n-----Postorder------")
postorder_traversal(new_bt)
print("\n-----Levelorder------")
levelorder_traversal(new_bt)
print("\n-----search------")
print(search_bt(new_bt, "Hoe"))

print("\n-----insert------")
newNode=TreeNode("Coffee")
print(insert_bt(new_bt, newNode))

levelorder_traversal(new_bt)
print(delete_node(new_bt, "Cold"))
levelorder_traversal(new_bt)
print(delete_bt(new_bt))
levelorder_traversal(new_bt)