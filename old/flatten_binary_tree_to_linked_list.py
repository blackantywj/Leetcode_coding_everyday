class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead
        """
        flattenUtil(root)
        # flatten(root.right)

def isChild(root):
    return root.left is None and root.right is None
        
def flattenUtil(root: TreeNode):
    if root is None or isChild(root):
        return root
    
    if root.left is not None and root.left.left:
        flattenUtil(root.left)
        
    temp=root.left
    if temp:
        while temp.right:
            temp=temp.right

        temp.right=root.right
        root.right=root.left
        root.left=None
        
    if root.right:
        flattenUtil(root.right)
    
    return root