class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check_p(s,l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        def dfs(i,path):
            if i==len(s):
                res.append(path[:])
                return
            for j in range(i,len(s)):
                if check_p(s,i,j):
                    path.append(s[i:j+1])
                    dfs(j+1,path)
                    path.pop()
        res = []
        dfs(0,[])
        return res