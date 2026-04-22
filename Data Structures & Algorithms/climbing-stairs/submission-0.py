class Solution:
    def climbStairs(self, n: int) -> int:
        """
        1.State: dp[i] represent the distinct ways to climb at i stairs
        2.Transition: dp[i] = dp[i-1]+dp[i-2]
        3.Base Case: dp[0] = 1 dp[1] = 1  dp[2] = dp[1]+dp[0]
        4.Final Solution: dp[n]
        """
        if n<=1:
            return 1
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]


        