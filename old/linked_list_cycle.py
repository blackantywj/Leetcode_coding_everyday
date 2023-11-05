class Solution:
    # def hasCycle(self, head: ListNode) -> bool:
    #     dic = {}
    #     pvalue = 0
    #     p = head
    #     while pvalue != dic['{}'.format(pvalue)]:
    #         if p == None:
    #             return False
    #         dic['{}'.format(p.value)] = p.value
    #         p = p.next
    #     return True
    def hasCycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False