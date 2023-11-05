class Solution:

    def __init__(self):
        self.data = {}
        
    def rightSideView(self, root: TreeNode, level=0) -> List[int]:
        if root:
            if not self.data.get(level):
                self.data[level] = root.val
            
            self.rightSideView(root.right, level+1)
            self.rightSideView(root.left, level+1)      
        return self.data.values()