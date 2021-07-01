class Solution:
    def jump(self, nums: List[int]) -> int:
        
        nums.reverse()
        n=len(nums)
        ran=range(1,n)
        
        dp=[sys.maxsize]*n
        dp[0]=0
        for i in ran:
            
            ran1=range(1,nums[i]+1)
            for j in ran1:
                
                dp[i]=min(dp[i],dp[max(0,i-j)]+1)
                
           return dp[n-1]
    
# class Solution:
#     def jump(self, nums:List[int])->int:
#         nums.reverse()
#         n=len(nums)
#         ran=range(1, n)
        
#         dp = [sys.maxsize]*n
#         dp[0]=0
#         for i in ran:
#             ran1 = range(1, nums[i]+1)
#             for j in ran1:
                
#                 dp[i]=min(dp[i], dp[max(0, i-j)]+1)
#             return dp[n-1]