class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left<right:
            mid = left+(right-left)//2
            if nums[0]>nums[-1]:
                if nums[mid]>nums[-1]:
                    left = mid + 1
                else:
                    right = mid
            else:
                return nums[0]
        return nums[left]