class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_map = {}
        n = len(nums)
        for i in nums:
            freq_map[i] = freq_map.get(i,0) + 1
        
        treshold = n // 3
        result = []

        for key in freq_map:
            if freq_map[key] > treshold:
                result.append(key)
        
        return result
        
         