class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # maxelement = max(nums)
        # return nums.index(maxelement)
        maxvalue = -2 ** 31
        maxindex = 0
        for i, element in enumerate(nums):
            if element > maxvalue:
                maxvalue = element
                maxindex = i
                
<<<<<<< HEAD
        return maxindex
=======
        return maxindex
>>>>>>> 192284b0e5bae3db598e96e0a4267b85cab9ace8
