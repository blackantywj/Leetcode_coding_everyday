class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        leftHeight = self.countNodesHelper(root, 0)
        rightHeight = self.countNodesHelper(root, 1)

        if leftHeight == rightHeight:
            return pow(2, leftHeight) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        

    def countNodesHelper(self, root, side):
        if root == None:
            return 0
        
        if side == 0:
            return 1 + self.countNodesHelper(root.left, side)
        else:
            return 1 + self.countNodesHelper(root.right, side)