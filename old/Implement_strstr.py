class Solution:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack == '':
            return 0
        if haystack != '' and needle == '':
            return 0
        for i, element in enumerate(haystack):
            if element == needle[0]:
                if haystack[i:len(needle)+i] == needle:
                    return i
                else:
                    continue
            else:
                continue
        return -1
    # def strStr(self, haystack: str, needle: str) -> int:
    #     if len(needle) == 0: return 0
    #     for i in range(0, len(haystack)-len(needle)+1):
    #         if haystack[i:i+len(needle)] == needle:
    #             return i
    #     return -1
cc = Solution()

print(cc.strStr('a', ''))