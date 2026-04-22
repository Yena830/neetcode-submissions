class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(opens,closes):
            if(opens == closes == n):
                res.append(''.join(stack))
            if opens > closes:
                stack.append(')')
                backtrack(opens,closes+1)
                stack.pop()
            if opens < n:
                stack.append('(')
                backtrack(opens+1,closes)
                stack.pop()
        backtrack(0,0)
        return res


            
        