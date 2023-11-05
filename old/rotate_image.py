class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        resultmid , result = [], []
        for j in range(0, len(matrix)+1):
            resultmid = []
            if j - len(matrix) == 0:
                break
            resultmid = [matrix[i][j] for i in range(len(matrix)-1, -1, -1)]

            result.append(resultmid)
        return result

cc = Solution()

print(cc.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))