class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        check = sum(nums)
        nums = [str(num) for num in nums]

        if check == 0:
            return '0'

        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] + nums[j + 1] < nums[j + 1] + nums[j]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        result = ""
        for s in nums:
            result += s

        return result
