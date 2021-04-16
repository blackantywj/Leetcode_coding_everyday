class Solution:
    def connect1(self, root):
        if root and root.left and root.right:
            root.left.next = root.right
            if root.next: # ***
                root.right.next = root.next.left # *
            self.connect(root.left) #当你执行到下一层的时候root.left.next(***)处是指向root.right的 因此*的作用就体现了出来
            self.connect(root.right)
    
    # BFS       
    def connect2(self, root):
        if not root:
            return 
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                queue.append(curr.left)
                queue.append(curr.right)
        
    # DFS 
    def connect(self, root):
        if not root:
            return 
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                stack.append(curr.right)
                stack.append(curr.left)