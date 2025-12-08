class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        prefixSum = 0

        for i in range(n):
            prefixSum += gain[i]
            gain[i] = prefixSum
        
        if max(gain) < 0:
            return 0
        
        return max(gain)