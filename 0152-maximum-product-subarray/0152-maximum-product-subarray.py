class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_so_far = nums[0]
        max_so_far = nums[0]
        maxProduct = nums[0]
        n = len(nums)

        for i in range(1, n):
            if nums[i] < 0:
                min_so_far, max_so_far = max_so_far, min_so_far

            min_so_far = min(nums[i], min_so_far * nums[i])
            max_so_far = max(nums[i], max_so_far * nums[i])

            maxProduct = max(maxProduct , max_so_far)
        
        return maxProduct
