def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root is None:
            return None
      
        temp = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        root.left = temp
        
        return root