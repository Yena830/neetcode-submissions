class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        res = [0]*2
        while(left<right):
            mid = (left+right)//2
            if numbers[left] +numbers[right] > target:
                if numbers[mid]+numbers[left] >target: 
                    right = mid
                else:
                    right -=1
            elif numbers[left] +numbers[right] < target:
                if numbers[mid]+numbers[right] <target:
                    left = mid
                else:
                    left +=1
            else:
                res[0]=left+1
                res[1]=right+1
                return res
        return res