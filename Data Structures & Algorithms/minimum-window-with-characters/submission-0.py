class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_dict = Counter(t)
        window = defaultdict(int)
        left = 0
        have = 0
        need = len(need_dict)
        res_len = float('inf')
        res = [-1,-1]

        for right, c in enumerate(s):
            window[c] +=1
            if c in need_dict and window[c] == need_dict[c]:
                have +=1
            while have == need:
                if right - left + 1 < res_len:
                    res = [left,right]
                    res_len = right - left + 1
                window[s[left]] -=1
                if s[left] in need_dict and window[s[left]]<need_dict[s[left]]:
                    have -=1
                left +=1
        return s[res[0]:res[1]+1] if res_len != float('inf') else ""
                
