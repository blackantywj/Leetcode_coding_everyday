# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     # head = listNode()
    #     head = None
    #     r = None
    #     if l1.val >= l2.val:
    #         head = l2
    #         l2 = l2.next
    #     else:
    #         head = l1
    #         l1 = l1.next
    #     r = head
    #     while l1 != None and l2 != None:
    #         if l1.val > l2.val:
    #             r.next = l2
    #             l2 = l2.next
    #         else:
    #             r.next = l1
    #             l1 = l1.next
    #     if l1 != None:
    #         r = l1
    #     elif l2 != None:
    #         r = l2
    #     return head
        def mergeTwoLists(self, l1, l2):
            dummy = cur = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 or l2
            return dummy.next
            
        def mergeTwoLists2(self, l1, l2):
            if not l1 or not l2:
                return l1 or l2
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

