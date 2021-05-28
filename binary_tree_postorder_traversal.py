def postorderTraversal(self, root):
        self.res=[]
        self.solve(root)
        return self.res
    
    def solve(self,root):
        if not root: return
        self.solve(root.left)
        self.solve(root.right)
        self.res.append(root.val)