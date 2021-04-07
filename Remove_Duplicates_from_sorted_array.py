class Solution:
    # def removeDuplicates(self, nums) -> int:
    #     flag = 0
    #     for i, element in enumerate(nums):
    #         if element in nums[0:i-1-flag]:
    #             nums.remove(element)
    #             flag += 1
    #         else:
    #             continue
    #     return len(nums)

    def removeDuplicates(self, nums) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return len(nums)
nums = [0,0,1,1,1,2,2,3,3,4]


cc = Solution()

result = cc.removeDuplicates(nums)
print(result)