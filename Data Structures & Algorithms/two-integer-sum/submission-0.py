class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = defaultdict(int)
        for i,num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target - num],i]
            num_dict[num] = i
        return [-1,-1]
