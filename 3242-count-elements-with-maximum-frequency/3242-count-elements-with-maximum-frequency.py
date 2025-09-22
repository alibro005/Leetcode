class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        max_freq = max(freq.values())
        
        result = 0
        for value in freq.values():
            if value == max_freq:
                result += value

        return result

        
