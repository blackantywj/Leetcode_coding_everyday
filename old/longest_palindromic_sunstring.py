# class Solution:
#     def longestPalindrome(self, s) -> str:
#         # midstr = int(len(str) - 1)
#         dic = {}
#         max1 = ''
#         for i, element in enumerate(s):
#             if element not in dic:
#                 dic[element] = i
#                 print(dic)
#             else:
#                 len1 = s[dic[element]:i+1]
#                 if len(len1) > len(max1):
#                     max1 = len1
#         if len(s) != 0 and len(max1) == 0:
#             max1 = s[0]
#         return max1

# 以上为首位相同子串的代码，而回文结构为AbbbbA 诸如此类

# class Solution:
#     def longestPalindrome(self, s) -> str:
#         # midstr = int(len(str) - 1)
#         dic = {}
#         max1 = ''
#         for i, element in enumerate(s):
#             if element not in dic:
#                 dic[element] = i
#                 # print(dic)
#             else:
#                 len1 = s[dic[element]:i+1]
#                 mid = len(len1) / 2
#                 if type(mid) == 'int':
                    
#                 else:
#                     mid = int(mid)
#                 print(list(s[mid + dic[element]:i+1]), list(s[dic[element]:mid+ dic[element]]))
#                 if self.string_reverse1(s[mid + dic[element]:i+1]) == s[dic[element]:mid + dic[element] + 1] and len(len1) > len(max1):
#                     max1 = len1
                
#                 elif self.string_reverse1(s[mid + dic[element]:i+1]) != s[dic[element]:mid + dic[element] + 1]:
#                     dic[element] = i
#         if len(s) != 0 and len(max1) == 0:
#             max1 = s[0]
#         print(max1)
#         return max1
    
#     def string_reverse1(self, string):
#         return string[::-1]


'''
遇到这样的一个问题，奇偶数无法正确识别✔
总是奇数的时候正确。
'''

class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        print(res)
        return res
    # get the longest palindrome, l, r are the middle indexes   
            # from inner to outer
    def helper(self, s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            return s[l+1:r]

stringtest = 'abuacjjjjaccaacba'

cc = Solution()

cc.longestPalindrome(stringtest)

'''
对于奇偶数回文组进行分开查找，直到找到最长的回文组

分治
'''