class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        intervals.append(newInterval)
        for i in sorted(intervals, key=lambda x: x[0]):
            if res and i[0] <= res[-1][-1]:
                res[-1][-1] = max(res[-1][-1], i[-1])
            else:
                res.append(i)
        return resw
