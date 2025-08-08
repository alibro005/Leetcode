class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in num_map:
                return [num_map[remaining], i]
            num_map[num] = i

        