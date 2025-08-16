class Solution:
    def checkXMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for i in range(0, n):
            for j in range(0, n):
                if i == j or i == n - 1 - j:
                    if matrix[i][j] == 0:
                        return False
                else:
                    if matrix[i][j] != 0:
                        return False
        return True
