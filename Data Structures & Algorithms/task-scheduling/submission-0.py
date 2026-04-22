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
        maxfreq = max(count.values())
        maxCount = sum(1 for v in count.values() if v==maxfreq)
        res = (maxfreq - 1) * (n + 1) + maxCount
        return max(res,len(tasks))
        

