# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return None
        stack=[(root,f'{root.val}')]
        path=[]
        while stack:
            root,val=stack.pop()
           
            if root.left==None and root.right==None:
                path.append(val)
            else:
                if  root.left:
                    stack.append((root.left,val+'->'+f'{root.left.val}'))
                if  root.right:
                    stack.append((root.right,val+'->'+f'{root.right.val}'))
        
        return path