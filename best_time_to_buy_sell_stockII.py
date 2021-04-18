class Solution:
    def maxProfit(self, prices):
        lenp = len(prices)

        ans = 0


        for i in range(1, lenp):
            ans += max(0, prices[i] - prices[i-1])

        return ans

pro = [7,1,5,3,6,4]

cc = Solution()

print(cc.maxProfit(pro))