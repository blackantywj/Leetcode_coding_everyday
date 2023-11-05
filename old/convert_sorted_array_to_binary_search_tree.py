# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    # 12:37
    def sortedArrayToBST(self, num):
        if not num:
            return None

        mid = len(num) // 2

        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])

        return root
# donot use the slice
def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
	return self.helper(nums, 0, len(nums))

def helper(self, nums, lower, upper):
	if lower == upper:
		return None

	mid = (lower + upper) // 2
	node = TreeNode(nums[mid])
	node.left = self.helper(nums, lower, mid)
	node.right = self.helper(nums, mid+1, upper)

	return node