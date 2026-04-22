class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        letters1 = [0] *26
        letters2 = [0] *26
        for i in range(len(s1)):
            letters1[ord(s1[i])-ord('a')] +=1
        
        k = len(s1)
        for i in range(len(s2)):
            letters2[ord(s2[i])-ord('a')] +=1
            if i<k-1:
                continue
            if letters1 == letters2:
                return True
            letters2[ord(s2[i-k+1])-ord('a')] -=1
        return False