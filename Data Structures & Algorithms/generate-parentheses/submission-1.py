class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(op,path):
            if len(path)==2*n:
                res.append("".join(path))
                return
            if op<n:
                path.append('(')
                dfs(op+1,path)
                path.pop()
            close = len(path)-op
            if op>close:
                path.append(')')
                dfs(op,path)
                path.pop()
        dfs(0,[])
        return res