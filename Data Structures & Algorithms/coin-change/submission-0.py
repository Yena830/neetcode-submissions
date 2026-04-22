class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        1.State:dp[i] represent at amount i, the min coins
        2.Transition: for each coin
                        if i>=coin:
                            dp[i] = min(dp[i],dp[i-coin]+1)
        3.Base case: dp[0] = 0
        4.Final solution:dp[amount]
        """
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i>=coin:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        return dp[amount] if dp[amount] !=float('inf') else -1