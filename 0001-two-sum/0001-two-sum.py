class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in num_map:
                return [num_map[remaining], i]
            num_map[num] = i

        # n = len(nums)

        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return -1
