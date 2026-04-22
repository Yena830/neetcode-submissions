class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        count = Counter([val for row in board for val in row])
        count_w = Counter(word)
        for key in count_w.keys():
            if key not in count:
                return False
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        def dfs(r,c,i):
            if i==len(word):
                return True
            if r<0 or c<0 or r>=m or c>=n or word[i]!=board[r][c] or board[r][c]=='#':
                return False
            board[r][c]='#'
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res
        for r in range(m):
            for c in range(n):
                if dfs(r,c,0):
                    return True
        return False