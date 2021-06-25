# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         total = 0
#         while n != 0:
#             crc = n % 2
#             n = n / 2
#             if crc == 1:
#                 total += 1
#         return total
    
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count