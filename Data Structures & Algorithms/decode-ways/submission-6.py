class Solution:
    def numDecodings(self, s: str) -> int:
        """
        if s[i-1] is '1' or '2' it could combine with s[i] '14' '23' 
            but '2' cannot with number bigger than '6'
        if s[i]=='0' means it should combine with s[i-1] ->'10'

        1.state:dp[i] represent end at ith char how many ways can be decode
        2.transition: if s[i]=='0'-> dp[i] = dp[i-1]
                      else:
                        dp[i] += dp[i-1]

                      if s[i-1]=='1' dp[i] = dp[i-1]+dp[i-2]
                      if s[i-1]=='2' and s[i]<'7' dp[i] = dp[i-1]+dp[i-2]
        3.base case: if s[0]=='0' dp[0] = 0
                     else: dp[0]=1
        4.final: dp[len(s)-1]
        """
        n = len(s)
        dp = [0]*n
        if not s or s[0]=='0':
            return 0
        dp[0] = 1
        for i in range(1,n):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i] = dp[i-2] if i >= 2 else 1
    
            else:
                dp[i] = dp[i-1]
                if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                    dp[i] += dp[i-2] if i >= 2 else 1
        return dp[-1]