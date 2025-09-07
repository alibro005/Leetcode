class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        for i in range(1 - n, n, 2):
            result.append(i)

        return result
