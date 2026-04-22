class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use mono stack
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                stackI= stack.pop()
                res[stackI] = (i - stackI)
            stack.append(i)
        return res