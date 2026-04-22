class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        minheap = []
        for key,val in count.items():
            heapq.heappush(minheap,(val,key))
            if len(minheap) > k:
                heapq.heappop(minheap)
        res = []
        for val, key in minheap:
            res.append(key)
        return res