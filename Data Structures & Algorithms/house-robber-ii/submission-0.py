class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        1.State: dp[i] represent at ith house
        2.Transition: dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        3.Base: dp[0] = nums[0] dp[1] = nums[1]
        4. Final: dp[-1]
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        def calculate(array):
            dp = [0]*len(array)
            for i in range(len(array)):
                if i == 0:
                    dp[i] = array[0]
                elif i == 1:
                    dp[i] = max(array[0], array[1])
                else:
                    dp[i] = max(dp[i-2]+array[i],dp[i-1])
            return dp[-1]
        return max(calculate(nums[:n-1]),calculate(nums[1:]))
        
