class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      
        xor_all = 0
        xor_arr = 0
        n = len(nums)
        
        for i in range(n + 1):
            xor_all ^= i  # XOR of 0 to n
        
        for num in nums:
            xor_arr ^= num  # XOR of elements in array
            
        return xor_all ^ xor_arr  # Missing number
