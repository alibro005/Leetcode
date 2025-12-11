class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        j = n

        for i in range(0,n):
            ans.append(nums[i])
            ans.append(nums[j+i])
        return ans
