class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        U:
        input: 2d list heights,heights[r][c] height fo curr level
                water can flow to cell height[cell]<= curr_height
                four directions (up, down, left, or right)
                water at edges can flow to ocean
        output: all the [r,c] can flow to P and A
                2d list [[r,c],[r',c']]
        
        1. start from four edges cells
        2. dfs(r,c,visited)
        
        pacific->left up
        atlantic->right down

        
        left = height >= max_height of left
        right = height >=max_height of right
        up
        down

        return max_height
        3. two set
        A
        P
        look for the intersection
        """
        m,n = len(heights),len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(r,c,visited):
            height = heights[r][c]
            visited.add((r,c))
            for dr,dc in [(-1,0),(0,-1),(0,1),(1,0)]:
                nr,nc = r+dr,c+dc
                if nr<0 or nc<0 or nr>=m or nc>=n or ((nr,nc) in visited) or heights[nr][nc]<height:
                    continue
                dfs(nr,nc,visited)
        for r in range(m):
            dfs(r,0,pacific)
            dfs(r,n-1,atlantic)
        for c in range(n):
            dfs(0,c,pacific)
            dfs(m-1,c,atlantic)
        res = []
        for (r,c) in pacific:
            if (r,c) in atlantic:
                res.append([r,c])
        return res


