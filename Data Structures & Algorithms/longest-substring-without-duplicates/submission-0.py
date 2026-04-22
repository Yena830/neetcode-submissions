class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in letter:
                letter.remove(s[left])
                left +=1
            letter.add(s[right])
            res = max(res, right - left + 1)
        return res
