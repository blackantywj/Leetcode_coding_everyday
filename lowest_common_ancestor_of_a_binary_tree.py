# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # O(n) time complexity and space complexity
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Goal - To find lowest common ancestor
        recursively check l and r and centre
        """
        res = None
        found = False
        def search(node):
            nonlocal res
            nonlocal found
            if not node:
                return 0
            cur = 0
            l = search(node.left)
            r = search(node.right)
            cur += l
            cur += r
            if node == p or node == q:
                cur += 1
            if cur == 2 and not found:
                res = node
                found = True
            return cur
        search(root)
        return res