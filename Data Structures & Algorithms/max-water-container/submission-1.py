class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        water = 0
        while left < right:
            if heights[left]< heights[right]:
                water = max(water, heights[left]*(right-left))
                left +=1
            else:
                water = max(water, heights[right]*(right-left))
                right -=1
        return water