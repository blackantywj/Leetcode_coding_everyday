# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         sum_money_1 = 0
#         sum_money_2 = 0
#         # if n % 2 == 0:
#         for i in range(0, len(nums), 2):
#             sum_money_1 += nums[i]
#         # else:
#         for i in range(1, len(nums), 2):
#             sum_money_2 += nums[i]
#         return max(sum_money_1, sum_money_2)

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0]*(len(nums)+1)
        memo[0] = 0
        memo[1] = nums[0]
        for i in range(2, len(nums)+1):
            memo[i] = max(nums[i-1] + memo[i-2], memo[i-1])
        return max(memo)