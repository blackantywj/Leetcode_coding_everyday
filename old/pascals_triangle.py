from operator import add
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for _ in range(1, numRows):
            map_ = map(add, [0] + res[-1], res[-1] + [0])
            res.append(list(map_))
        return res if numRows else []
    # def generate(self, numRows):
    #         res = [[1]]
    #         for i in range(1, numRows):
    #             res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
    #         return res[:numRows]
    # def generate(self, numRows: int):
    #     resultlist = []
    #     for i in range(0, numRows):
    #         resultlist.append(self.func(i))
    #     return resultlist
    def func(self, numRows):
        resultlist = []
        for i in range(0, numRows+1):
            h = self.Combinatorial(numRows, i)
            resultlist.append(h)
        return resultlist
    def Combinatorial(self, n,i):
        '''设计组合数'''
        #n>=i
        Min=min(i,n-i)
        result=1
        for j in range(0,Min):
            result=result*(n-j)/(Min-j)
        return round(result)

cc = Solution()

print(cc.generate(9))


'''
def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]
'''