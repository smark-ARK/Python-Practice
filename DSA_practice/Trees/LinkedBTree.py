from BinaryTree import BinaryTree
from DSA_practice.LinkedLists.Singly.LinkedQueue import LinkedQueue


class LinkedBTree(BinaryTree):
    class _Node:
        __slots__ = ["_element", "_parent", "_left", "_right"]

        def __init__(self, _element, _parent=None, _left=None, _right=None):
            self._element = _element
            self._parent = _parent
            self._left = _left
            self._right = _right

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self.container = container
            self.node = node

        def element(self):
            return self.node._element

        def __eq__(self, other):
            return type(self) is type(other) and self.node is other.node

    def validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("P must be of a proper Position Type")
        if p.container is not self:
            raise ValueError("P is not of same tree")
        if p.node.parent is p.node:
            raise ValueError("Node on P is deprecated")
        return p.node

    def make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self.root = None
        self.size = 0

    def is_root(self, p):
        node = self.validate(p)
        return node is self.root

    def root(self):
        return self.make_position(self.root)

    def num_children(self, p):
        node = self.validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def left(self, p):
        node = self.validate(p)
        return self.make_position(node._left)

    def right(self, p):
        node = self.validate(p)
        return self.make_position(node._right)

    def __len__(self):
        return self.size

    def parent(self, p):
        node = self.validate(p)
        return self.make_position(node._parent)

    def add_root(self, e):
        if self.root is not None:
            raise ValueError("Root already exists")
        self.root = self._Node(e)
        self.size = 1
        return self.make_position(self.root)

    def add_left(self, p, e):
        node = self.validate(p)
        if node._left is not None:
            raise ValueError("left node already exists")
        node._left = self._Node(e, node)
        self.size += 1
        return self.make_position(node._left)

    def add_right(self, p, e):
        node = self.validate(p)
        if node._right is not None:
            raise ValueError("right node already exists")
        node._right = self._Node(e, node)
        self.size += 1
        return self.make_position(node._right)

    def replace(self, p, e):
        node = self.validate(p)
        old = node._element
        node._element = e
        return old

    def delete(self, p):
        node = self.validate(p)
        if self.num_children(p) == 2:
            raise ValueError("P has 2 children")
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self.root:
            self.root = child
        parent = node._parent
        if node is parent._left:
            parent._left = child
        else:
            parent._right = child
        self.size -= 1
        node._parent = node
        return node._element

    def attatch(self, p, t1, t2):
        node = self.validate(p)
        if self.num_children(p) is not 0:
            raise ValueError("p is not Leaf")
        if not type(self) is type(t1) is type(t2):
            raise TypeError("All 3 must be trees")
        self.size += t1.__len__() + t2.__len__()
        if not t1.is_empty():
            t1.root._parent = node
            node._left = t1.root
            t1.root = None
            t1.size = 0
        if not t2.is_empty():
            t2.root._parent = node
            node._left = t2.root
            t2.root = None
            t2.size = 0

    def preorder(self):
        if not self.is_empty():
            for p in self._preorder_subtree(self.root()):
                yield p

    def _preorder_subtree(self, p):
        yield p
        for c in self.children(p):
            for other in self._preorder_subtree(c):
                yield other

    def postorder(self):
        if not self.is_empty():
            for p in self._postorder_subtree(self.root()):
                yield p

    def _postorder_subtree(self, p):
        for c in self.children(p):
            for other in self._preorder_subtree(c):
                yield other
        yield p

    def breadth_first_traversal(self):
        fringe = LinkedQueue()
        fringe.enqueue(self.root())
        while not fringe.is_empty():
            p = fringe.dequeue()
            yield p
            for c in self.children(p):
                fringe.enqueue(c)

    def inorder(self):
        if not self.is_empty():
            for p in self._postorder_subtree(self.root()):
                yield p

    def _inorder_subtree(self, p):
        if self.left(p) is not None:
            for other in self._inorder_subtree(p):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._inorder_subtree(p):
                yield other

