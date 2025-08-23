class Solution:
    # def lowerBound(self,nums,target):
    #     n = len(nums)
    #     left , right = 0 , n - 1

    #     ans = n

    #     while left <= right:
    #         mid = left + (right-left)//2

    #         if nums[mid] >= target:
    #             ans = mid
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #     return ans

    def searchInsert(self, nums: List[int], target: int) -> int:
        # return self.lowerBound(nums,target)
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
