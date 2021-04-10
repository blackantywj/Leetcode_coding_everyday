class Solution:
    def searchInsert(self, nums, target: int) -> int:
        i = 0 
        if target <= nums[0]:
            return 0
        while i < len(nums):
                if i+1 == len(nums):
                    if target > nums[i]:
                        return i+1
                    else:
                        return i
                if target > nums[i] and target < nums[i+1]:
                    return i+1
                if target == nums[i] and target < nums[i+1]:
                    return i
                

                i += 1
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         if target in nums:
#             return nums.index(target)
#         if max(nums) < target:
#             return len(nums)
#         for idx in range(len(nums)):
#             if target < nums[idx]:
#                 return idx
#             elif target >= nums[idx] and target - nums[idx] < 0:
#                 return idx
nums = [1, 3, 5, 6]

target = 

cc = Solution()

result = cc.searchInsert(nums, target)

print(result)