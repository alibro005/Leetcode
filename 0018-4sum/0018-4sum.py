class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    l = target - (nums[i] + nums[j] + nums[k])

                    total_sum = nums[i] + nums[j] + nums[k] + l

                    if l in nums[k+1:]:
                        temp = [nums[i],nums[j],nums[k],l]
                        
                        if temp not in result:
                            result.append(temp)
        return result