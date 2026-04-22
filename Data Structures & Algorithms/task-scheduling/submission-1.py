class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        1.get freq map first
        2.Example:{'X':2,'Y':2}->
        {'A':3,'B':2,'C':1} 3+3*(3-1)
        A-> O -> O -> O -> A -> O -> O -> O -> A  
        {'A':3,'B':3,'C':3} (n+1)*(maxfreq - 1)+maxCount
        """
        count = Counter(tasks)
        maxheap = []
        for val in count.values():
            heapq.heappush(maxheap,-val)
        queue = deque()
        res = 0
        while maxheap or queue:
            res +=1
            if maxheap:
                c = heapq.heappop(maxheap) + 1
                if c != 0:
                    queue.append((c,res+n))
            if queue and queue[0][1] == res:
                heapq.heappush(maxheap,queue[0][0])
                queue.popleft()
        return res

