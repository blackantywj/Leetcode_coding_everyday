def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = [root]
        out = []
        if not root:
            return None
        
        while(len(queue) > 0):
            node = queue.pop(0)
            out.append(node.val)
            if node.right:
                queue.insert(0,node.right)
            if node.left:
                queue.insert(0,node.left)
       
        return out


def preorderTraversal(self, root):
	queue = [root]
	out = []

	if not root:
		return None
	while(len(queue) > 0):
		node = queue.pop(0)
		out.append(node.val)
		if node.right:
			queue.insert(0, node.right)
		if node.left:
			queue.insert(0, node.left)
'''


'''