class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        d = k % n

        def reverse(nums, left: int, right: int):

            while left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

            return nums

        reverse(nums, 0, n - 1)
        reverse(nums, 0, d-1)
        reverse(nums, d, n-1)
