class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)
        for s in strs:#O(n)
            # key = ''.join(sorted(s)) #O(nlogn)
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')]+=1
            key = tuple(count)
            str_map[key].append(s)
        return list(str_map.values())