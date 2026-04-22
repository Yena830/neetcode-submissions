class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_water = 0
        while(left<right):
            curr_left = heights[left]
            curr_right = heights[right]
            if curr_left < curr_right:
                max_water = max(max_water,(right-left)*curr_left)
                left += 1
            else:
                max_water = max(max_water,(right-left)*curr_right)
                right -=1
        return max_water