class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        result = binary.count('1')

        return result
