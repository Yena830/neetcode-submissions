class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix[0])-1
        up = 0
        down = len(matrix) - 1
        mid_row = -1
        while(up <= down):
            mid_row = up+(down-up)//2
            if matrix[mid_row][-1] < target:
                up = mid_row+1
            elif matrix[mid_row][0] > target:
                down = mid_row-1
            else:
                break
        

        while(left <= right):
            mid_col = left+(right-right)//2
            if matrix[mid_row][mid_col] < target:
                left = mid_col +1
            elif matrix[mid_row][mid_col] >target:
                right = mid_col -1
            else:
                return True
        return False
