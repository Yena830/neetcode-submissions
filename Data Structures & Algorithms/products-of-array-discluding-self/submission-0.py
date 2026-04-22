class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] *len(nums)
        left = 1
        right = 1
        # Calculate the left
        for i in range(len(nums)):
            res[i] *=left
            left *=nums[i]
        # Calcualate the right
        for j in range(len(nums)-1,-1,-1):
            res[j] *=right
            right *= nums[j]
        return res
