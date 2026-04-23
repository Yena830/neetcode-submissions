class TrieNode:
    def __init__(self):
        self.son = {}
        self.end = None
    
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.son:
                node.son[c] = TrieNode()
            node = node.son[c]
        node.end = word
    


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = PrefixTree()
        m,n = len(board),len(board[0])
        for word in words:
            trie.insert(word)
        res =[]
        def dfs(i,j,node):
            if i<0 or j<0 or i>=m or j>=n or board[i][j]=='#' or board[i][j] not in node.son:
                return
            c = board[i][j]
            board[i][j] = '#'
            node = node.son[c]
            if node.end:
                res.append(node.end)
                node.end = None
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                dfs(i+dx,j+dy,node)
            board[i][j] = c
        for r in range(m):
            for c in range(n):
                dfs(r,c,trie.root)
        return res
            