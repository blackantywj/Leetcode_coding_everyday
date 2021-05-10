'''
https://stackoverflow.com/questions/6951792/a-b-not-the-same-as-a-a-b
'''
class Solution:
    def merge(self, intervals):
        if len(intervals)==0:
            return []
        if len(intervals)==1:
            return intervals
        intervals = sorted(intervals, key = lambda x: x[0])
        blank = intervals[0]
        res = []
        
        for i in range(1,len(intervals)):
            
            if intervals[i][0]<=blank[1]:
                blank = [blank[0],max(intervals[i][1],blank[1])]
                
            else:
                res.append(blank)
                blank = intervals[i]
        res.append(blank)
                
        return res

cc = Solution()

cc.merge([[1,3],[2,6],[8,10],[15,18]])