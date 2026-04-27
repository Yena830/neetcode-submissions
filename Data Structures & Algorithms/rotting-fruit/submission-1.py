class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        fresh = 0
        queue = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    fresh +=1
                elif grid[r][c]==2:
                    queue.append((r,c,0))
        step = 0
        while queue:
            r,c,step = queue.popleft()
            for dr,dc in [(-1,0),(0,-1),(0,1),(1,0)]:
                nr,nc = r+dr,c+dc
                if nr<0 or nc<0 or nr>=m or nc>=n or grid[nr][nc]!=1:
                    continue
                queue.append((nr,nc,step+1))
                grid[nr][nc] = 2
                fresh -=1
        return step if fresh == 0 else -1

        