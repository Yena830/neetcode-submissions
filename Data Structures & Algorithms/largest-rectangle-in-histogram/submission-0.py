class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #[(index,height)]
        max_area = 0
        # loop the list
        for i,h in enumerate(heights):
            start = i
            # if the current hight is smaller
            while len(stack)>0 and stack[-1][1]>h:
                index,height = stack.pop()
                # update the max area
                max_area = max(height*(i-index),max_area)
                start = index
            #Add non-decreasing height into stack
            stack.append((start,h))

        #Check if stack is remaining 
        if stack:
            for i,h in stack:
                max_area = max(h*(len(heights)-i),max_area)
        return max_area
