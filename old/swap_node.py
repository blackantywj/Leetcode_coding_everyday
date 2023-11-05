# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         p = head
#         listresult = []
#         result = ListNode()
#         i=0
#         while p != None:
#             listresult.append(p.val)
#             p = p.next
#         if len(listresult) <= 1:
#             return head
#         # print(listresult)
#         while i < len(listresult)-1:
#             listresult[i], listresult[i+1] = listresult[i+1], listresult[i]
#             i += 2
#         # print(listresult)
#         p = result
#         for i, element in enumerate(listresult):
#             # print(element)
#             p.val = element
#             if i < len(listresult)-1:
#                 newp = ListNode()
#                 p.next = newp
#                 p = newp
#         return result
class Solution:
    def swapPair(self, head):
        pre, pre.next = self, head

        while pre.next and pre.next.next:
            a = pre.next

            b = a.next

            pre.next, b.next, a.next = b, a, b.next

            pre = a
        return self.next