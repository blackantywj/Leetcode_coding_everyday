# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left != None:
            return 1 + self.minDepth(root.left)
        if root.right != None:
            return 1 + self.minDepth(root.right)
        leftMinDepth = self.minDepth(root.left)
        rightMinDepth = self.minDepth(root.right)
        return 1 + min(leftMinDepth, rightMinDepth)
        # if root.left != None or root.right != None:
        #     depth_left_min = self.minDepth(root.left)
        #     depth_right_min = self.minDepth(root.right)
        # else:
        #     return 
            