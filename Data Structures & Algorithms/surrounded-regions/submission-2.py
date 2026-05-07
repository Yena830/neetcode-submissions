class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        input: board 'x''o'
        modify in place

        if 'o' surrounded by 'X' four directions->change to 'X'
        """
        if not board or not board[0]:
            return
        m,n = len(board), len(board[0])
        # dfs
        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n or board[r][c]!='O':
                return
            board[r][c] = 'E' # turn 'O' to 'E'
            # search four neighbors
            for dr,dc in [(-1,0),(0,-1),(1,0),(0,1)]:
                dfs(r+dr,c+dc)
        
       
        
        # start from edges-> find 'O'
        for r in range(m):
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][n-1]=='O':
                dfs(r,n-1)
        for c in range(n):
            if board[0][c] == 'O':
                dfs(0,c)
            if board[m-1][c] == 'O':
                dfs(m-1,c)


        # go through board again turn 'O' to 'X' and 'E' to 'O'
        for r in range(m):
            for c in range(n):
                if board[r][c]=='O':
                    board[r][c] = 'X'
                elif board[r][c]=='E':
                    board[r][c] ='O'