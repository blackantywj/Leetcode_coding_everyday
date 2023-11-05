def maxProduct(self, nums: List[int]) -> int:        
	ans = -math.inf
	n = len(nums)
	mi,ma = 1,1
	for i in range(1,n+1):
		v = nums[i-1]
		new_mi = min(v,mi*v,ma*v)
		ma = max(v,ma*v,mi*v)
		mi = new_mi
		ans = max(ans,mi,ma)
	return ans