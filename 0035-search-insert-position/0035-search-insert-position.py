class Solution:
    def lowerBound(self,nums,target):
        n = len(nums)
        left , right = 0 , n - 1

        ans = n

        while left <= right:
            mid = left + (right-left)//2

            if nums[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.lowerBound(nums,target)