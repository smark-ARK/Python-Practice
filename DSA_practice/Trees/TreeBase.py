class TreeBase:
    class Position:
        def element(self, p):
            raise NotImplementedError("Subclass must implement it")

        def __eq__(self, other):
            raise NotImplementedError("Subclass must implement it")

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        raise NotImplementedError("Subclass must implement it")

    def is_root(self, p):
        return self.root == p

    def parent(self, p):
        raise NotImplementedError("Subclass must implement it")

    def num_children(self, p):
        raise NotImplementedError("Subclass must implement it")

    def children(self, p):
        raise NotImplementedError("Subclass must implement it")

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def len(self):
        return len(self)

    def is_empty(self):
        return len(self) == 0

    def positions(self):
        raise NotImplementedError("Subclass must implement it")

    def iter(self):
        raise NotImplementedError("Subclass must implement it")

