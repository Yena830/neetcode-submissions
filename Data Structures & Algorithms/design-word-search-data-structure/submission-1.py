class TrieNode:
    def __init__(self):
        self.son = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.son:
                node.son[c] = TrieNode()
            node = node.son[c]
        node.end = True
        

    def search(self, word: str) -> bool:
        def dfs(i,node):
            for j in range(i,len(word)):
                if word[j] == '.':
                    for child in node.son.values():
                        if dfs(j+1,child):
                            return True
                    return False
                else:
                    if word[j] not in node.son:
                        return False
                    node = node.son[word[j]]
            return node.end
        return dfs(0,self.root)
        
