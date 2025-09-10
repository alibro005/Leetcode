class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        map_diagonal = dict()

        for i in range(n):
            for j in range(m):
                if i + j not in map_diagonal:
                    map_diagonal[i + j] = []
                map_diagonal[i + j].append(mat[i][j])

        result = []

        for k in range(n + m - 1):
            if k % 2 == 0:
                result.extend(map_diagonal[k][::-1])
            else:
                result.extend(map_diagonal[k])
        return result
