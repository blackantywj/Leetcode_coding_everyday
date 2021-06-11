class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        ans = '-' if numerator // denominator < 0 else ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        prefrac = numerator // denominator
        ans += str(prefrac) 
        
        rem = numerator % denominator
        if not rem:
            return ans
        ans += '.'
        remainder = ''
        seen = {}
        
        while rem not in seen:
            if rem == 0:
                return ans + remainder
            
            seen[rem] = len(remainder)
            rem *= 10
            remainder += str(rem//denominator)
            rem %= denominator
            
        return ans + remainder[:seen[rem]] + '(' + remainder[seen[rem]:] + ')' 
