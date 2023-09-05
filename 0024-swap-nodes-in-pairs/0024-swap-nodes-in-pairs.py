# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        cur = head
        
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
            
        return head
        