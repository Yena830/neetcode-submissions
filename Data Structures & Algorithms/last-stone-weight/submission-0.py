class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for stone in stones:
            heapq.heappush(maxheap,-stone)
        while len(maxheap)>1:
            stone1 = -heapq.heappop(maxheap)
            stone2 = -heapq.heappop(maxheap)
            if stone1!=stone2:
                heapq.heappush(maxheap,-(stone1-stone2))
        return -maxheap[0] if maxheap else 0