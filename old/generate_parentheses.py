class Solution:
    def generateParenthesis(self, n: int):
        stack = []
        res = []
        
        def backstack(on, cn):
            if on == cn == n:
                res.append("".join(stack))
                return
            if on < n:
                stack.append('(')
                backstack(on+1, cn)
                stack.pop()
            if cn < on:
                stack.append(')')
                backstack(on, cn+1)
                stack.pop()
                
        backstack(0, 0)
        print(res)
        return res

n = 3

cc = Solution()

cc.generateParenthesis(n)