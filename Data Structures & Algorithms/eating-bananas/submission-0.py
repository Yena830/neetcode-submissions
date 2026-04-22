class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Use binary search
        #if the h=n, then k = max
        #when h>n ->  0<k<max
        # 1<=k<=max
                
        # The min speed is 1, and get the max value of piles
        left = 1
        right = max(piles)

        # while loop for binary search
        while(left < right):
            k = left + (right - left)//2
            
            #Calculate the time needed to finsh under k speed
            time = 0
            for p in piles:
                time += -(-p // k)
            
            #search
            # When time is bigger than h, means we need a faster speed, update the left
            if time > h:
                left = k + 1
            # When the time is smaller or equal to h, koko can finish the banana in time, but we can try to find a smaller speed to eat
            else:
                right = k
        
        # while loop end when right is equal than left, so the left is the correct answer
        return left