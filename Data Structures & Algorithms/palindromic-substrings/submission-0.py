class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        1.state:dp[i][j] represent if s[i:j+1] is pd or not
        2.transition: if i==j dp[i][j] = True
                      if s[i]==s[j] and j==i+1 dp[i][j] = True
                      if s[i]==[j] and dp[i+1][j-1]==True 
        every time dp[i][j]=True count+=1
        """
        count = 0
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i==j:
                    dp[i][j]=True
                    count+=1
                elif s[i]==s[j]:
                    if j==i+1:
                        dp[i][j] = True
                        count+=1
                    elif j>i+1 and dp[i+1][j-1]==True:
                        dp[i][j] = True
                        count+=1
        return count