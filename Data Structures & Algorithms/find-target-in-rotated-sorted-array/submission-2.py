class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #search space is [0,n-1]
        #find a k where nums[k]=target
        
        left = 0
        right = len(nums)-1


        #define a condition
        def condition(mid):
            if(nums[mid] > nums[-1]):
                return nums[-1]<target<= nums[mid]
            else:
                return target >nums[-1] or nums[mid] >= target

        
        while(left < right):
            mid = left+(right-left)//2
            if condition(mid):
                right = mid
            else:
                left = mid+1
        if(nums[left]==target):
            return left
        else:
            return -1