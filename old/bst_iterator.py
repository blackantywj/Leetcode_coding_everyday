class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack: List[TreeNode] = []
        self._initialize_stack(root)

    def _initialize_stack(self, root: Optional[TreeNode]):
        curr_node = root
        
        while curr_node is not None:
            self.stack.append(curr_node)
            curr_node = curr_node.left

    def next(self) -> int:
        top_node = self.stack.pop()

        if top_node.right is not None:
            curr_node = top_node.right

            while curr_node is not None:
                self.stack.append(curr_node)
                curr_node = curr_node.left

        return top_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0