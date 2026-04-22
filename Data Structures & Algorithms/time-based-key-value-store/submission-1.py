class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        arr = self.timemap[key]
        left = 0
        right = len(arr)
        while left<right:
            mid = left + (right-left)//2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        return arr[left-1][1] if left>0 else ""            
        
