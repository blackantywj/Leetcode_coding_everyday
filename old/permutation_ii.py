class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def helper(curr,nums,length,ret):
            if len(curr) == length:
                ret.append(curr)
            else:

                for i in range(len(nums)):
                    if i != 0 and nums[i] == nums[i-1]:
                        # skip the same number to avoid duplicates
                        pass
                    else:
                        curr.append(nums[i])
                        helper(list(curr),nums[:i]+nums[i+1:],length,ret)
                        curr.pop()
        nums.sort()
        ret = []
        helper([],nums,len(nums),ret)
        return ret
