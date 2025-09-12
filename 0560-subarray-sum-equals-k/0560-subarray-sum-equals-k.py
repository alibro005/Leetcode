class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq_map = {0:1}

        result = 0
        current_sum = 0

       

        for num in nums:
            current_sum += num
            check = current_sum - k

            if check in freq_map:
                result += freq_map[check]

            freq_map[current_sum] = freq_map.get(current_sum, 0) + 1
        
        return result
