import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        allzeros = True
        for num in nums:
            if num!=0:
                allzeros=False
                break
        if allzeros:
            return '0'
            
        def comparator(x, y):
            if x+y > y+x:
                return -1
            elif x+y < y+x:
                return 1
            else:
                return 0
        nums = sorted(map(str, nums), key=functools.cmp_to_key(comparator))
        return ''.join(nums)