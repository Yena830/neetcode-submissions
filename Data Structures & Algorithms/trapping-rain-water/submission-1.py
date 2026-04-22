class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        water = 0
        left_max = 0
        right_max = 0
        while left<right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max<right_max:
                water += max(0,left_max - height[left])
                left +=1
            else:
                water += max(0,right_max - height[right])
                right-=1
        return water