class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        1. State: dp[i] represent the min cost at i th floor
        2. Transition: dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        3. Base: dp[0] = 0 dp[1] = 0
        4. Final: dp[-1]
        """
        dp = [0] * (len(cost)+1)
        if len(cost)<=1:
            return 0
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[len(cost)]