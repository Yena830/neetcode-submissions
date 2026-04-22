class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append([timestamp,value])

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        arr = self.dict[key]
        left = 0
        right = len(arr)-1

        while(left<right):
            mid = left+(right-left+1)//2
            if arr[mid][0] <= timestamp:
                left = mid
            else:
                right = mid - 1
        if arr[left][0] <= timestamp:
            return arr[left][1]
        else:
            return ""


        
        
