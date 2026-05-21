class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        1.State: dp[i] represent at ith house
        2.Transition: dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        3.Base: dp[0] = nums[0] dp[1] = nums[1]
        4. Final: dp[-1]
        """
        n = len(nums)
        dp = [0]*n
        for i in range(n):
            if i==0:
                dp[i] = nums[i]
            elif i==1:
                dp[i] = max(dp[i-1],nums[i])
            else:
                dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[-1]