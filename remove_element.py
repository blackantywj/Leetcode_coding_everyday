class Solution:
    def removeElement(self, nums, val: int) -> int:
        nums.sort()
        flag = 0
        flag2 = 0
        for i, element in enumerate(nums):
            if element == val:
                flag = i
                break
        for element in nums:
            if element == val:
                flag2 += 1
        #print(flag, flag2)
        
                # nums.remove(element)
        return len(nums[0:i] + nums[i+flag2-1:])
    def removeElement_example(self, nums, val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
               nums[count] = nums[i]
               count += 1
        return count
nums = [2, 2, 3, 3]

cc = Solution()

cc.removeElement_example(nums, 3)