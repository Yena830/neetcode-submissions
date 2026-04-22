class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        if not digits:
            return []
        res = []
        def dfs(i,path):
            if i == len(digits):
                res.append(path)
                return
            for c in nums[int(digits[i])]:
                dfs(i+1,path+c)
    
        dfs(0,"")
        return res