class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #use stack to store all numbers
        number_stack = []
        res = 0
        for char in tokens:
            if char == '+':
                number_stack.append(number_stack.pop()+number_stack.pop()) 
            elif char == '-':
                number_stack.append(-number_stack.pop()+number_stack.pop())
            elif char == '*':
                number_stack.append(number_stack.pop()*number_stack.pop())
            elif char == '/':
                number_stack.append(int((1/float(number_stack.pop()))*number_stack.pop()))
            else:
                number_stack.append(int(char))
        return number_stack[0]