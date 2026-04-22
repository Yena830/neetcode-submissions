class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)<=len(nums2):
            arr1,arr2 = nums1,nums2 
        else:
            arr1,arr2 = nums2,nums1
        m,n = len(arr1),len(arr2)
        total = m+n
        left = 0
        right = m - 1
        while True:
            mid1 = left + (right - left)//2
            mid2 = total//2 - mid1 - 2
            arr1_left = arr1[mid1] if mid1 >=0 else float('-inf')
            arr1_right = arr1[mid1+1] if mid1<m-1 else float('inf')
            arr2_left = arr2[mid2] if mid2 >=0 else float('-inf')
            arr2_right = arr2[mid2+1] if mid2<n-1 else float('inf')

            if arr1_left<=arr2_right and arr2_left<=arr1_right:
                if total % 2 == 0:
                    return (max(arr1_left,arr2_left)+min(arr1_right,arr2_right))/2
                else:
                    return float(min(arr1_right,arr2_right))
            elif arr1_left>arr2_right:
                right = mid1 - 1
            elif arr2_left>arr1_right:
                left = mid1 + 1