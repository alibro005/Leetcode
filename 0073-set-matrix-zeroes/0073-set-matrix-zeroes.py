class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        rowtrack = [0 for _ in range(rows)]
        coltrack = [0 for _ in range(cols)]

        for i in range(0,rows):
            for j in range(0,cols):
                if matrix[i][j] == 0:
                    rowtrack[i] = -1
                    coltrack[j] = -1

        for i in range(0,rows):
            for j in range(0,cols):
                if rowtrack[i] == -1 or coltrack[j] == -1:
                    matrix[i][j] = 0
                    
        

