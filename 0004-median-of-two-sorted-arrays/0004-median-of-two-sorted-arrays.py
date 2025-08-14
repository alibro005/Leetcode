class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        l = len(merged)

        start = 0
        end = l - 1

        while start <= end:
            mid = start + (end - start) // 2

            if l % 2 == 0:
                return (merged[mid] + merged[mid + 1]) / 2
            else:
                return merged[mid]
