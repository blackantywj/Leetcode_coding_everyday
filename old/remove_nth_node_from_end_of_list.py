# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # p = head
        # m = head
        # lens = 0
        # i = 0
        # # list1 = []
        # if n == 1 and m.next == None:
        #     head = m.next
        #     print('1')
        #     return head
        # while p != None:
        #     # list1.append(p.val)
        #     lens += 1
        #     p = p.next
        # # print(lens)
        # while m != None:
        #     if i == lens-n-1:
        #         m.next = m.next.next
        #         # print('1')
        #         # print(m.val)
        #     else:
        #         m = m.next
        #     i+=1
        # return head
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        a=head
        c=0
        while(a):
            a=a.next
            c+=1         #C is size of list
        ans=c-n+1        #Ans is the index of element that is to be removed 
        a=head
        if c==1:         #If list is containing only one element
            return 
        if ans-1==0:     #If list has 2 elements and we have to remove the first element
            return a.next
        while(ans-1>1):  #For all other cases and if [1,2] and n=1 then for that it'll not run & execute last command
            a=a.next
            ans-=1
        a.next=a.next.next   
        return(head)

head = ListNode()

head.val = 1
head.next = None

n = 1
cc = Solution()

cc.removeNthFromEnd(head, n)
                
        