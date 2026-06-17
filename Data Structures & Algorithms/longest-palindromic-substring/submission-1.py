class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        two pointers
        start at every center(odd/even) and try to expand while s[left]==s[right]
        """
        curr_len = 0
        res = ""
        for i in range(len(s)):
            # odd center
            left = i
            right = i
            while left>=0 and right<len(s) and s[left]==s[right]:
                if right-left+1>curr_len:
                    res = s[left:right+1]
                    curr_len = right-left+1
                left -=1
                right +=1
            # even center
            left = i
            right = i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                if right-left+1>curr_len:
                    res = s[left:right+1]
                    curr_len = right-left+1
                left -=1
                right +=1
        return res
