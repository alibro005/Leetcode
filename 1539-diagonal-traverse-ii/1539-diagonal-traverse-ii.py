class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        n = len(mat)

        freq = dict()

        for i in range(n):
            for j in range(len(mat[i])):
                if i + j not in freq:
                    freq[i + j] = []
                freq[i + j].append(mat[i][j])

        result = []

        for i in sorted(freq.keys()):
            result.extend(freq[i][::-1])
    
        return result
