from TreeBase import TreeBase


class BinaryTree(TreeBase):
    def right(self, p):
        raise NotImplementedError("Subclass must implement it")

    def left(self, p):
        raise NotImplementedError("Subclass must implement it")

    def sibling(self, p):
        if self.is_root(p):
            return None
        parent = self.parent(p)
        if p == self.left(parent):
            return self.right(parent)
        if p == self.right(parent):
            return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

