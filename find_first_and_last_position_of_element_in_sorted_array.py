# class Solution:
# 	def searchRange(self, nums, target):
# 		index = {}
# 		if len(nums) == 0:
# 			return [-1, -1]
# 		for i, element in enumerate(nums):
# 			if element == target:
# 				index[i] = i
# 			elif element < target:
# 				continue
# 			elif element > target:
# 				return self.func(index)
# 		return self.func(index)
# 	def func(self, index):
# 		if index == {}:
# 			return [-1, -1]
# 		else:
# 			list1 = [i for i in index]
# 			return [list1[0], list1[-1]]

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        def bisect_left(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l if nums[l] == target else -1

        def bisect_right(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2 + 1
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m
            return l if nums[l] == target else -1

        return [bisect_left(nums, target), bisect_right(nums, target)]


cc = Solution()

cc.searchRange([1], 1)