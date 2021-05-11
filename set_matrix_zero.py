class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix
        for i in len(matrix):
            for j in len(matrix[0]):
                if m[i][j] == 0:
                    matrix = setzero(i, j, matrix)
        
        
    def setzero(self, i, j, m):
        for e in enumerate(len(m[0])):
            m[i][e] = 0
        for e in enumerate(len(m)):
            m[e][j] = 0
        return m