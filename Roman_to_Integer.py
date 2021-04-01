class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        if len(s) == 0:
            return 0
        sum = 0
        i=0
        while i < len(s):
            
            if s[i] in {'I', 'X', 'C'} and s[i:i+2] in dic:
                sum += dic[s[i:i+2]]
                i += 2        

            else:
                sum += dic[s[i]]
                i += 1

        print(sum)
        
teststr = 'IX'

cc = Solution()

cc.romanToInt(teststr)