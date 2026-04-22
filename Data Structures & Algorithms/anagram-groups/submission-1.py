class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            str_map[key].append(s)
        return list(str_map.values())