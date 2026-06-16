class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        two pointers
        for every center, try to expand if s[i]==s[j]
            odd center
            even center
        count every palindrome

        """ 
        res = 0
        def helper(l,r):
            left=l
            right = r
            count = 0
            while left>=0 and right<=len(s)-1 and s[left]==s[right]:
                count +=1
                left -=1
                right +=1
            return count
        for i in range(len(s)):
            res +=helper(i,i)
            res +=helper(i,i+1)
        return res
