# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         dic = []
#         corrent = numRows - 1
#         list = range(corrent+1) + range(corrent).reverse


            

#         print(result)
# teststring = 'PAYPALISHIRING'

# cc = Solution()

# cc.convert(teststring, 3)
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)