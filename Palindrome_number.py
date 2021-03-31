class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        if x < 0:
            return False

        elif len(str(x)) % 2 == 0:
            flag = int(len(str(x)) / 2)

            if strx[0:flag][::-1] == strx[flag:]:
                return True
            else:
                return False 
        else:
            flag = int(len(str(x)) / 2)
            if strx[0:flag][::-1] == strx[flag+1:]:
                return True
            else:
                return False

x = 12321434

cc = Solution()

print(cc.isPalindrome(x))
