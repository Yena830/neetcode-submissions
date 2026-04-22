class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        up = 0
        down = m-1
        while up < down:
            mid = up+(down-up)//2
            if matrix[mid][-1]<target:
                up = mid + 1
            else:
                down = mid

        left = 0
        right = n-1
        while left<right:
            mid = left+(right-left)//2
            
            if matrix[up][mid]<target:
                left = mid + 1
            else:
                right = mid

        return True if matrix[up][left]==target else False
