class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ans, level = 0, [root]
        while root and level:
            # print(root)
            ans += 1
            LRpair = [(node.left, node.right) for node in level]
            # print([leaf for LR in LRpair])
            level = [leaf for LR in LRpair for leaf in LR if leaf] # God code
            # print(level)
            # flag += 1
        return ans