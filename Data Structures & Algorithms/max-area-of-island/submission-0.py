class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        similar to the number of island
        input: a 2-d array, 1 land 0 water
        output: the max area of island

        1.for each cell, search land
        2.if find land, do dfs
        3.count current area
        """
        m = len(grid)
        n = len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n or grid[r][c]!=1:
                return
            grid[r][c] = 2
            nonlocal area
            area +=1
            for dr,dc in [(-1,0),(0,-1),(1,0),(0,1)]:
                dfs(r+dr,c+dc)
        
        res = 0
        for r in range(m):
            for c in range(n):
                area = 0
                if grid[r][c]==1:
                    dfs(r,c)
                res = max(res,area)
        return res