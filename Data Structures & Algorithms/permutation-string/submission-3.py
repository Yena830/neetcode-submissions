class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        length = len(s1)
        count = [0]*26
        for c in s1:
            count[ord(c)-ord('a')]+=1
        left = 0
        freq = [0]*26
        for right,c in enumerate(s2):
            freq[ord(c)-ord('a')] +=1
            if right - left + 1< length:
                continue
            if count == freq:
                return True
            freq[ord(s2[left])-ord('a')]-=1
            left+=1
        return False
            

