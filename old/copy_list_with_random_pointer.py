"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None: return
        
        #step1 put copy of each node in the middle of given list
        curr = head
        while curr:
            temp = curr.next 
            curr.next = Node(curr.val)
            curr.next.next = temp
            curr = temp
            
        #step2 set random pointer
        curr = head
        while curr:
            if curr.random: #random could point to null
                curr.next.random = curr.random.next 
            if curr.next:# to make sure next is not null
                curr = curr.next.next 
            else:
                curr = curr.next 
        
        #step3 fix the pointers of original and clone list
        original = head
        clone = head.next 
        '''
        o c
        3 3 4 4 5 5
        '''
        curr = clone
        while clone and original:
            if original.next:
                original.next = original.next.next 
            if clone.next:
                clone.next = clone.next.next 
            original = original.next 
            clone = clone.next 
            
        return curr 