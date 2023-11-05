class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n
        # if n>0:

        #     return x * self.myPow(x, n-1)
        # if n<0:
        #     if abs(n) == 0:
        #         return 1
        #     return 1/x * self.myPow(1 / x, n + 1)
		# if n == 0:
		# 	return 1

cc = Solution()
print(cc.myPow(2, -2))

class Solution:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)

class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow


