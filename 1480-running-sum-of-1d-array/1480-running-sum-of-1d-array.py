class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixSum = 0
        for i in range(n):
            prefixSum += nums[i]
            nums[i] = prefixSum
        return nums



