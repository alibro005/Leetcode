class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = 0, n - 1

        while start <= end:
            mid = start + (end - start) // 2

            left = nums[mid - 1] if mid - 1 >= 0 else float("-inf")
            right = nums[mid + 1] if mid + 1 < n else float("-inf")

            if nums[mid] > left and nums[mid] > right:
                return mid
            elif nums[mid] > right:
                end = mid - 1
            else:
                start = mid + 1
        
