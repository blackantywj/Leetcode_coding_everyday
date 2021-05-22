# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        headcopy = ListNode()
        p = head
        if head == None:
            return head
        list = []
        while p != None:
            list.append(p.val)
            p = p.next
        # print(list)
        list.sort()
        headcopy.val = list[0]
        p = headcopy
        for i in list[1:]:
            newnode = ListNode()
            newnode.val = i
            p.next = newnode
            p = p.next
            
        return headcopy