# 3sum.py

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            # if i >= 1 and v == nums[i-1]:
            #     continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 2 # 我现在有了v和x，我现在需要一个-v-x，三数相加就是0，因此可以建立字典对i+1的数据进行遍历
                else:
                    res.add((v, -v-x, x))
            print(res)
        return [*map(list, res)]

nums = [0, 0, 0]

cc = Solution()

print(cc.threeSum(nums))