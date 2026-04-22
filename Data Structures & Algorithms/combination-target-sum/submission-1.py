class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(i,num):
            if num == 0:
                res.append(path[:])
                return
            if i==len(nums):
                return
            if nums[i]<=num:
                path.append(nums[i])
                dfs(i,num-nums[i])
                path.pop()
            dfs(i+1,num)
            
        dfs(0,target)
        return res
            
