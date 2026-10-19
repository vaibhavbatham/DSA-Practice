# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        curr = head
        length = 0

        while curr != None:
            length += 1 
            curr = curr.next

        if length == n :
            return head.next

        curr = head
        traverse = length - n -1
        
        for i in range (traverse):
            curr= curr.next

        curr.next = curr.next.next
        return head

         