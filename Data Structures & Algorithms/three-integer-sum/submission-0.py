class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Use two pointers
        # Sort the nums list first
        nums = sorted(nums)
        res =[]
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while(j<k):
                sums = nums[i]+nums[j]+nums[k]
                if sums > 0:
                    k -= 1
                elif sums < 0:
                    j += 1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    # have to check until j is not the same number
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
        return res