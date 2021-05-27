"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if root is None:
            return None
        
        original_root = root
        
        while root:
            
            next_level_first_node = Node(0)
            cur_child = next_level_first_node
            while root:
                if root.left:
                    cur_child.next = root.left
                    cur_child = cur_child.next
                if root.right:
                    cur_child.next = root.right
                    cur_child = cur_child.next
                root = root.next
                
            root = next_level_first_node.next
                    
        return original_root  
        