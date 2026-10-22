# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        
        if head is None or head.next is None:
            return head
        
        length = 0
        curr = head

        while curr != None:
            curr = curr.next
            length += 1

        k = k % length 
        
        for i in range(k):
            prev = head
            while prev.next.next != None:
                prev = prev.next

            temp = head
            curr = prev.next

            curr.next = temp
            prev.next = None
            head = curr

        return head