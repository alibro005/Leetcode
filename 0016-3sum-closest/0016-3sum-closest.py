class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        closest_sum = float("inf")
        best = None

        for i in range(n):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                if abs(total_sum - target) < closest_sum:
                    closest_sum = abs(total_sum - target)
                    best = total_sum

                if total_sum < target:
                    j += 1
                elif total_sum > target:
                    k -= 1
                else:
                    return total_sum

        return best
