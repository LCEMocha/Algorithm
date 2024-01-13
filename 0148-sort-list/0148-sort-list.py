# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        li = []
        while p:
            li.append(p.val)
            p = p.next
        
        li.sort()
        
        p = head
        for i in range(len(li)):
            p.val = li[i]
            p = p.next
        return head