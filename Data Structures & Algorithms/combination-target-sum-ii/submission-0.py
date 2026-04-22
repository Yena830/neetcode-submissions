class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        
        def dfs(i,num):
            if num == 0:
                res.append(path[:])
                return
            if i == len(candidates):
                return
            if candidates[i]<=num:
                path.append(candidates[i])
                dfs(i+1,num-candidates[i])
                path.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,num)
        dfs(0,target)
        return res