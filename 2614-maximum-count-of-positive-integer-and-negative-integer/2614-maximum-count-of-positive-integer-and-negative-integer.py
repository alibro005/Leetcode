class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        n = len(nums)
        for i in range(0, n):
            if nums[i] > 0:
                pos += 1
            elif nums[i] < 0:
                neg += 1

        result = max(pos, neg)
        return result
