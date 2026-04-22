class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter = {}
        left = 0
        res = 0
        for right in range(len(s)):
            if s[right] in letter and letter[s[right]] >=left:
                left = letter[s[right]] + 1
            letter[s[right]] = right
            res = max(res, right - left + 1)
        return res
