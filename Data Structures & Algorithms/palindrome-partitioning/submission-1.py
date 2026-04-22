class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(s,left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left +=1
                right -=1
            return True
        def dfs(i,path):
            if i==len(s):
                res.append(path[:])
                return
            for j in range(i,len(s)):
                if check(s,i,j):
                    path.append(s[i:j+1])
                    dfs(j+1,path)
                    path.pop()
        res = []
        dfs(0,[])
        return res
