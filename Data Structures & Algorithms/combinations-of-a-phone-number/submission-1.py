class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        if not digits:
            return []
        res = []
        def dfs(i,path):
            if i == len(digits):
                res.append("".join(path))
                return
            for c in nums[int(digits[i])]:
                path.append(c)
                dfs(i+1,path)
                path.pop()
        dfs(0,[])
        return res