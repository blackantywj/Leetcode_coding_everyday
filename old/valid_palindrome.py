import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sy = re.findall('[0-9a-zA-Z]', s)
        print(str(sy))
        print( str(sy[::-1]).lower())
        return str(sy).lower() == str(sy[::-1]).lower()

class Solution:
    def isPalindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s==s[::-1]

cc = Solution()

print(cc.isPalindrome("0a"))