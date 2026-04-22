class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        length = len(s1)
        count = Counter(s1)
        left = 0
        freq = defaultdict(int)
        for right,c in enumerate(s2):
            freq[c] +=1
            if right - left + 1< length:
                continue
            if count == freq:
                return True
            freq[s2[left]]-=1
            if freq[s2[left]] == 0:
                del freq[s2[left]]
            left+=1
        return False
            

