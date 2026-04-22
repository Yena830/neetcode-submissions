class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = defaultdict(int)
        left = 0
        res = 0
        maxf = 0
        for right,c in enumerate(s):
            letters[c] +=1
            maxf = max(maxf, letters[c])
            while (right - left + 1) - maxf > k:
                letters[s[left]] -=1
                left +=1
            res = max(res,right-left+1)

        return res

