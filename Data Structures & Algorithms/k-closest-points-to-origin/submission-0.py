class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x,y in points:
            distance = math.sqrt((x - 0)**2 + (y - 0)**2)
            heapq.heappush(minheap,(distance,(x,y)))
        res = []
        for _ in range(k):
            _,(x,y) = heapq.heappop(minheap)
            res.append([x,y])
        return res

        