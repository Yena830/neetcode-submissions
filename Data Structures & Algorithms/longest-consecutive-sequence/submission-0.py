class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Use hash set, turn the list into a set
        numSet = set(nums)
        longest = 0
        for num in numSet:
            #if the current number could be the first number of the sequence
            if num-1 not in numSet:
                length = 1
                #Find the next consecutive one
                while (num+length) in numSet:
                    length +=1
                longest = max(length, longest)
        return longest