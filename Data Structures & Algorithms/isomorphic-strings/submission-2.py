class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letter1 = {}
        letter2 = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            c1,c2 = s[i], t[i]
            if c1 not in letter1 and c2 not in letter2:
                letter1[c1]=c2
                letter2[c2]=c1
            elif c1 not in letter1 or c2 not in letter2:
                return False
            else:
                if letter1[c1]!=c2 or letter2[c2]!=c1:
                    return False
        return True