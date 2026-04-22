class Solution:
    def isValid(self, s: str) -> bool:
        # Use stack
        self.stack = []
        self.brackets = {')':'(', '}': '{', ']':'['}
        for char in s:
            # if the char is a close one
            if char in self.brackets:
                # check if the stack already has char inside and the last one is the pair open bracket
                if len(self.stack)>0 and self.stack[-1] == self.brackets[char]:
                    # pop the last item
                    self.stack.pop()
                else:
                    return False
            else:
                self.stack.append(char)
        #if the stack is empty
        if len(self.stack) == 0:
            return True
        else:
            return False