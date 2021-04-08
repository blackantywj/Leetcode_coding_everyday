class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2: return

        # solve 2-sum
        if N == 2:
            l,r = 0,len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums)-N+1):   # careful about range
                if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                    self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        return
    '''
    递归的思路非常值得借鉴！！！
    '''
    # def fourSum(self, nums, target: int):
    #         """
    #         :type nums: List[int]
    #         :rtype: List[List[int]]
    #         """
    #         b = []
    #         if len(nums) < 4:
    #             return []
    #         nums.sort()
    #         res = set()
    #         for j, m in enumerate(nums[:-2]):
    #             # if j >= 1 and m == nums[j-1]:
    #             #     continue
    #             # if m == -1:
    #             #     print("2")
    #             for i, v in enumerate(nums[:-2]):
    #                 if i == j:
    #                     continue
    #                 d = {}
    #                 for k, x in enumerate(nums[i+1:]):
    #                     if x not in d:
    #                         d[-v-x-m+target] = 1 
    #                     else:
    #                         res.add((m, v, -v-x-m+target, x))
    #                 # print(res)
    #         result = [*map(list, res)]
    #         for i in result:
    #             i.sort()
    #             if i not in b:
    #                 b.append(i)
    #         return b


    # def removeDuplicates(self, nums) :
    # # 对列表进行循环修改时要使用nums[:]而不是nums
    #     for n in nums:
    #         if nums.count(n) > 1:
    #             nums.remove(n)
    #     return nums
nums = [-3, -1, 0, 2, 4, 5]
target = 0
b=[]
cc = Solution()

result = cc.fourSum(nums, target)

for i in result:
    i.sort()
    if i not in b :
        b.append(i)

print(b)