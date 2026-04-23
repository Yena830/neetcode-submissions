class TrieNode:
    # use hashmap to store the children of node
    def __init__(self):
        self.son = {}
        self.end = False
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            # if c not show in Trie
            if c not in node.son:
                node.son[c] = TrieNode()
            node = node.son[c]
        # mark the end of the word
        node.end = True


    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.son:
                return False
            node = node.son[c]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.son:
                return False
            node = node.son[c]
        return True
        
        