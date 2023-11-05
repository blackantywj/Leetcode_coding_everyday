# class Solution:
#     def maxProfit(self, prices) -> int:
#         i = 1
#         j = len(prices) - 1
#         maxresult = 0
#         # if len(prices) == 2:
#         #     if prices[1] - prices[0] > 0:
#         #         return prices [1] - prices[0]
#         #     else:
#         #         return 0
#         while i <= len(prices) - 1:
#             if  prices[j-i+1] - min(prices[0:j-i+1]) > maxresult:
#                 maxresult = prices[j-i+1] - min(prices[0:j-i+1])
#             i += 1
#         return maxresult
# class Solution(object):
#     def maxProfit(self, prices):
#         low = float('inf')
#         profit = 0
#         for i in prices:
#             profit = max(profit, i-low)
#             low = min(low, i)
#         return profit

class Solution(object):
    def maxProfit(self, prices):
        maxcur = 0
        maxsofar = 0
        i = 1
        while i < len(prices):
            maxcur+=(prices[i] - prices[i-1])
            maxcur = max(0, maxcur)
            maxsofar = max(maxcur, maxsofar)
            i+=1
        return maxsofar
cc = Solution()

print(cc.maxProfit([7, 1, 5, 2, 4, 6]))