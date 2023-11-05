class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        res = 0
        curr_sign = 1
        while i < len(s):
            if s[i].isdigit():
                curr_res, i = self._get_num(s, i)
            elif s[i] == '*':
                next_num, i = self._get_num(s, i+1)
                curr_res *= next_num
            elif s[i] == '/':
                next_num, i = self._get_num(s, i+1)
                curr_res //= next_num
            elif s[i] == '+' or s[i] == '-':
                res += curr_sign * curr_res
                curr_sign = 1 if s[i] == '+' else -1
                curr_res = None
                i+= 1
            else:
                i += 1
        
        return res + curr_sign*curr_res

    def _get_num(self, s, idx):
        """
        Assume s[idx] is a digit or some spaces followed by a digit, 
        return the number starting from s[idx] as well as the next index
        """
        assert s[idx].isdigit() or s[idx] == ' '
        while s[idx] == ' ':
            idx += 1
        
        res = ''
        while idx < len(s) and s[idx].isdigit():
            res += s[idx]
            idx += 1
        return int(res), idx