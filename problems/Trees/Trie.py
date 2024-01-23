class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_str = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for i in word:
            node = current.children.get(i)
            if not node:
                node = TrieNode()
            current.children.update({i: node})
            current = node
        current.end_of_str = True
        print("inserted successfully")

    def search(self, word):
        current = self.root
        for i in word:
            node = current.children.get(i)
            if node is None:
                return False
            current = node
        return True if current.end_of_str else False


def delete(root: TrieNode, word: str, index: int = 0):
    ch = word[index]
    node = root.children.get(ch)
    can_delete = False

    if len(root.children) > 1:
        delete(node, word, index + 1)
        return False

    if index == len(word) - 1:
        if len(root.children) > 1:
            root.end_of_str = False
            return False
        else:
            root.children.pop(ch)
            return True

    if node.end_of_str == True:
        delete(node, word, index + 1)
        return False
    can_delete = delete(root, word, index + 1)

    if can_delete == True:
        root.children.pop(ch)
        return True
    else:
        return False


new_trie = Trie()

new_trie.insert("ARK")
new_trie.insert("SM")
new_trie.insert("ARJ")
new_trie.insert("SMARK")
print(new_trie.search("SM"))
delete(new_trie.root, "SM")
print(new_trie.search("SM"))
