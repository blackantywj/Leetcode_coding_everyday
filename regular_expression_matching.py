class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        eq = bool(s) and p[0] in [s[0], '.'] 

        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (eq and self.isMatch(s[1:], p)) 
        else:
            return eq and self.isMatch(s[1:], p[1:])

s = 'apppp'

p = '.*'

cc = Solution()

print(cc.isMatch(s, p))