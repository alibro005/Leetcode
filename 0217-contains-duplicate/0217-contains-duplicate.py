from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq_map = dict()

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
            
            if freq_map[num] > 1:
                return True

        return False
