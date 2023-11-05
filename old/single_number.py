class Solution:
    def singleNumber(self, nums) -> int:
        for index, element in enumerate(nums):
            # if index == 0 and element not in nums[1:]:
            #     return element
            if element not in nums[:index] + nums[index+1:]:
                return element

class Solution:
    def singleNumber(self, nums):
        for i in range(1,len(nums)):
            nums[0] ^= nums[i]
        return nums[0]
nums = [4, 1,2,2 ,1]

cc = Solution()

print(cc.singleNumber(nums))