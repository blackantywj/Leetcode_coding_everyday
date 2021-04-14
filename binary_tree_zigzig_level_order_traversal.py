# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, level = [], [root]
        flag = 0
        while root and level:
            # print(root)
            ans.append([node.val for node in self.func(level, flag)])
            LRpair = [(node.left, node.right) for node in level]
            # print([leaf for LR in LRpair])
            level = [leaf for LR in LRpair for leaf in LR if leaf] # God code
            # print(level)
            flag += 1
        return ans
    def func(self, level, flag):
        if flag % 2 == 0:
            return level
        else:
            return level[::-1]

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res, temp, stack, flag=[], [], [root], 1
        while stack:
            for i in xrange(len(stack)):
                node=stack.pop(0)
                temp+=[node.val]
                if node.left: stack+=[node.left]
                if node.right: stack+=[node.right]
            res+=[temp[::flag]]
            temp=[]
            flag*=-1
        return res