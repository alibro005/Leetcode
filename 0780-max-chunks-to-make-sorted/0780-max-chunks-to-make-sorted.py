class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        a , b , c = 0 , 0 , 0
        n = len(arr)

        for i in range(n):
            a += arr[i]
            b += i

            if a == b:
                c += 1
        return c
