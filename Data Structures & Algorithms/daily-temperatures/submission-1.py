class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        U:
        find next warmer day for each day
        input: a list of temperature
        output: a list of how many day after can have a warmer temp

        M:
        monotonic stack
        
        P:
        inside stack: non-increasing
        once we meet temp > stack[-1] pop out and update

        """
        stack = []
        res = [0] * len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                index = stack.pop()
                res[index] = i-index
            stack.append(i)
        return res