# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def ch(root):
            if(root==None):
                return (0,1)
            if(root.left==None and root.right==None):
                return (1,1)
            x,y=ch(root.left)
            if(y==0):
                return x+1,y
            x=x+1
            a,b=ch(root.right)
            if(b==0):
                return a+1,b
            a=a+1
            if(abs(x-a)<2):
                return (max(x,a),1)
            return (max(x,a),0)
        x,y=ch(root)
        return y