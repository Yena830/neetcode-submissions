class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        condition: find minimun -> nums[left]>nums[mid] & nums[mid]<nums[right]
        if the list is rotated, the nums[k] must smaller or equal as nums[right]

        :type nums: List[int]
        :rtype: int
        """
        

        #intialize
        left = 0
        right = len(nums)-1

        #while loop [left,right]
        while(left<right):
            mid = left+(right-left)//2
            #condition: find minimun -> nums[left]>nums[mid] & nums[mid]<nums[right]
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
            