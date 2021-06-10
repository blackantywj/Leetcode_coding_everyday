# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
# #         numsdic = {}
        
# #         # dictionary
# #         for i, element in enumerate(nums):
# #             if element not in nums:
# #                 numsdic[element] = 0
# #             else:
# #                 numsdic[element] += 1
# #         print(numsdic)
        
# #         return None
# #         numsset = set(nums)
        
# #         for element in numsset:
# #             if nums.count(element) >= 
#         flag = 0
#         flagelement = ''
#         for element in nums:
#             if flagelement != element:
#                 flagelement = element
#                 flag = 1
#             else:
#                 flag += 1
#             if flag >= 3:
#                 # print(element)
#                 nums.remove(element)
#                 flag -= 1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        a = 2
        b = 2
        while a<n and b<n:
            if nums[a] > nums[a-1] or nums[a] > nums[a-2]:
                a = a+1
                if a==n:
                    return a
                
            if nums[a] == nums[b]:
                b = b+1
            elif (nums[a] !=nums[b]) and (nums[b] > nums[a-1] or nums[b] > nums[a-2]) and (b>a):
                nums[a],nums[b] = nums[b],nums[a]
                a += 1
                b +=1
            else:
                b +=1
        return a

if __name__ is "__main__":
	solo = Solution()

	solo.removeDuplicates([0,0,1,1,1,1,2,3,3])
