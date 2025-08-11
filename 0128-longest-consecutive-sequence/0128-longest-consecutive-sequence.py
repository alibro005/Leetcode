class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        last_smallest = float("-inf")
        longest = 0
        n = len(nums)

        for i in range(0, n):
            num = nums[i]
            if num - 1 == last_smallest:
                count += 1
                last_smallest = num
            elif num != last_smallest:
                count = 1
                last_smallest = num
            longest = max(longest, count)
        return longest
