class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {')':'(','}':'{',']':'['}
        stack = []
        for c in s:
            if c in bracket.keys():
                if not stack or stack[-1]!=bracket[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return True if not stack else False