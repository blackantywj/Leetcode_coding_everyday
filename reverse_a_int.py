# class Solution:
#     def reverse(self, x: int) -> int:
#         if x > 0:
#             result = self.string_reverse1(str(x))
#         else:
#             result = self.string_reverse2(str(x))
#         print(type(result))
#         print(result)
#     def string_reverse1(self, string):
#         return int(string[::-1])

#     def string_reverse2(self, string):
#         return int('-' + string[:0:-1])


# x = -123
# cc = Solution()

# cc.reverse(x)

class Solution:
    def reverse(self, x):
            """
            :type x: int
            :rtype: int
            """
            sign = lambda x: x and (1, -1)[x < 0]
            r = int(str(sign(x)*x)[::-1])
            return (sign(x)*r, 0)[r > 2**31 - 1]