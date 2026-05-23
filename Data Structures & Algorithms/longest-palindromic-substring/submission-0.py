class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        1. State:dp[i][j] represent start at ith end at jth
            True -> is palindrome 
            False -> not palindrome
        2. Transition: 
            
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
                
        3. Base Case:
            if i == j:
                dp[i][j] = True
            if j==i+1 and s[i]==s[j]:
                dp[i][j]=True
        4. Final:
            the longest j-i+1
            s[i:j+1]
        """
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        res = s[0]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i==j:
                    dp[i][j] = True
                if i+1==j and s[i]==s[j]:
                    dp[i][j] = True
                if i<n-1 and j>0 and j-i+1>2 and s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j-i+1>len(res):
                    res = s[i:j+1]
        return res
