class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        input: a 2d array, '0' water '1' land
        output: the number of island
        M:
        1.for each cell in grid
        2.if find land at curr cell -> start from curr cell
        3.dfs: mark as visited and search neighbors
        4.after every dfs count+=1

        TC:O(mn)
        SC:O(mn)

        """
        m = len(grid)
        n = len(grid[0])
        count = 0

        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n or grid[r][c]!='1':
                return
            grid[r][c] = '2'
            for dr,dc in [(-1,0),(0,-1),(1,0),(0,1)]:
                dfs(r+dr,c+dc)
        

        for r in range(m):
            for c in range(n):
                if grid[r][c]=='1':
                    dfs(r,c)
                    count +=1
        return count
