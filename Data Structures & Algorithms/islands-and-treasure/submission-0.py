class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid),len(grid[0])

        def dfs(r,c,step):
            if r<0 or c<0 or r>=m or c>=n or grid[r][c] == -1 or grid[r][c]<step:
                return
            grid[r][c] = min(grid[r][c],step)
            for dr,dc in [(-1,0),(0,-1),(1,0),(0,1)]:
                dfs(r+dr,c+dc,step+1)
            

        for r in range(m):
            for c in range(n):
                if grid[r][c]==0:
                    dfs(r,c,0)
        