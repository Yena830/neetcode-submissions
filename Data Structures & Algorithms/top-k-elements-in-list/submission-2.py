class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)] # because the largest freq could be n
        for num,freq in count.items():
            bucket[freq].append(num)
        res = []
        for freq in range(len(nums),-1,-1):
            for num in bucket[freq]:
                if len(res)<k:
                    res.append(num)
        return res