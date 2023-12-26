class BinaryTree:
    def __init__(self, size):
        self.max_size = size
        self.list = [None] * self.max_size
        self.last_used_index = 0

    def is_empty(self):
        return self.last_used_index == 0

    def is_full(self):
        return self.last_used_index + 1 >= self.max_size

    def insert(self, value):
        if self.is_full():
            return "Tree Already Full"
        self.list[self.last_used_index + 1] = value
        self.last_used_index += 1
        return f"added: {value}"

    def search(self, value):
        for i in self.list:
            if i == value:
                return "success"
        return "not found"

    def preorder_traversal(self, n=1):
        if n > self.last_used_index:
            return
        print(self.list[n])
        self.preorder_traversal(n * 2)
        self.preorder_traversal((n * 2) + 1)

    def inorder_traversal(self, n=1):
        if n > self.last_used_index:
            return
        self.inorder_traversal(n * 2)
        print(self.list[n])
        self.inorder_traversal((n * 2) + 1)

    def postorder_traversal(self, n=1):
        if n > self.last_used_index:
            return
        self.postorder_traversal(n * 2)
        self.postorder_traversal((n * 2) + 1)
        print(self.list[n])

    def levelorder_traversal(self):
        for i in range(1, self.last_used_index + 1):
            print(self.list[i])
        return

    def delete(self, value):
        for i in range(1, self.last_used_index + 1):
            if self.list[i] == value:
                self.list[i] = self.list[self.last_used_index]
                self.list[self.last_used_index] = None
                self.last_used_index -= 1
                return f"Deleted: {value}"
        return "Could not delete"

    def delete_self(self):
        self.list = None
        self.last_used_index = 0
        return "Tree deleted from the memory"


new_bt = BinaryTree(10)
print(new_bt.insert("Drinks"))
print(new_bt.insert("Hot"))
print(new_bt.insert("Cold"))
print(new_bt.insert("Tea"))
print(new_bt.insert("Coffee"))
print(new_bt.insert("Juice"))
print(new_bt.insert("Cola"))
print(new_bt.search("Hot"))
print("\n----Preorder-----")
new_bt.preorder_traversal(1)
print("\n----Inorder-----")
new_bt.inorder_traversal(1)
print("\n----Postorder-----")
new_bt.postorder_traversal(1)
print("\n----Levelorder-----")
new_bt.levelorder_traversal()
print("\n", new_bt.delete("Cold"))
print("\n----Levelorder-----")
new_bt.levelorder_traversal()
print("\n", new_bt.delete_self())
