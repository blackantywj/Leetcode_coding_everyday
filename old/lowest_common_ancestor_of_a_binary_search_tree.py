# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node1=p if p.val<q.val else q
        node2=q if q.val>p.val else p
        res= self.lcautil(root,node1,node2)
        return res
    
    def lcautil(self,root,node1,node2):
        if node1.val<=root.val and root.val<=node2.val:
            return root
        elif root.val>node1.val and root.val>node2.val:
            return self.lcautil(root.left,node1,node2)
        else:
            return self.lcautil(root.right,node1,node2)