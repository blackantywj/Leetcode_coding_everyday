class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i, element in enumerate(nums):
            if element not in dic:
                dic[element] = 1
            else:     
                dic[element] += 1
        # print(dic)
        
        return max(dic, key=dic.get)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
            